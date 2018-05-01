# -*- coding: utf-8
import re
import sys

"""
Updates tanzil.net's quran-uthmani-pause-marks.txt to match
the orthography of the latest Medinah mushaf.

See: https://github.com/alquran-foundation/quran-text
"""

tanween = {'ً': 'ࣰ', 'ٌ': 'ࣱ', 'ٍ': 'ࣲ'}
repls = [
    # Remove "not permissible to pause" marks (68 occurrences)
    ('ۙ ', ''),
    # Replace circle sukoon with head of khaa
    ('ْ', 'ۡ'),
    # Use the more semantically correct madd
    ('ٓ', 'ۤ'),
    # Remove spaces before pause marks
    (r' ([ۖۗۚۛۜ])', r'\1'),

    # Use U+06CC (Farsi Yeh) for all yaa positions,
    # instead of U+064A (Arabic Yeh) for starting and middle,
    # and U+0649 (Alef Maksura) for final and isolated
    ('ي', 'ی'),
    (r'ِ(ا۟)?ى|ى[ٌَُِّْ]', lambda m: m.group(0).replace('ى', 'ی')),

    # Replace tanween with harakah before meem al-iqlaab
    ('ًۢ', 'َۢ'),
    ('ٌۢ', 'ُۢ'),
    ('ٍۭ', 'ِۭ'),

    # Use open Tanween (U+08F0, U+08F1, U+08F2) in ikhfaa' and
    # idghaam cases, instead of regular Tanween (U+064B, U+064C, U+064D)
    (r'[ًٌٍ](?=[اى]?( [ۖۗۚۛۜ])?[ \n][تثجدذرزسشصضطظفقكلمنوي])', lambda m: tanween[m.group(0)]),
]

out_file = open('quran-uthmani.txt', 'w')
for ayah in open(sys.argv[1]):
    for r in repls:
        ayah = re.sub(r[0], r[1], ayah)
    out_file.write(ayah)
