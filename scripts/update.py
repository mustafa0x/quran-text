import re
import sys
import json

"""
Updates tanzil.net's quran-uthmani-pause-marks.txt to match
the orthography of the latest Medinah mushaf.

Usage: `python3 update.py quran-uthmani-pause-marks.txt`

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
    (r' ([ۖۗۚۛۜۘ])', r'\1'),

    # Use U+06CC (Farsi Yeh) for all yaa positions,
    # instead of U+064A (Arabic Yeh) for starting and middle,
    # and U+0649 (Alef Maksura) for final and isolated
    ('ي', 'ی'),
    (r'ِ(ا۟)?ى|ى[ٌَُِّۡ]', lambda m: m.group(0).replace('ى', 'ی')),

    # Replace tanween with harakah before meem al-iqlaab
    ('ًۢ', 'َۢ'),
    ('ٌۢ', 'ُۢ'),
    ('ٍۭ', 'ِۭ'),

    # An anamoly, especially as 'بَعۡدِ مَا' does have a space
    ('بَعۡدَمَا', 'بَعۡدَ مَا'),

    # Replace diamonds with dots (each occurs once).
    ('۪', 'ٜ'),
    ('۫', '۬'),

    # Unnecessary alif maksoorah
    ('یَٰصَىٰحِبَیِ', 'یَٰصَٰحِبَیِ'),

    # Use open Tanween (U+08F0, U+08F1, U+08F2) in ikhfaa' and
    # idghaam cases, instead of regular Tanween (U+064B, U+064C, U+064D)
    (r'[ًٌٍ](?=[اى]?[ۖۗۚۛۜۘ۟]?( ۩)?[ \n](۞ )?[تثجدذرزسشصضطظفقكلمنوی])', lambda m: tanween[m.group(0)]),

    # Use hamzah below
    (r'[ئؤ](?=[ࣲِ][ ۭۚ])', lambda m: {'ئ':'ی', 'ؤ': 'و'}[m.group(0)] + 'ٕ'),
]

def replace_word(s, change):
    words = s.split(' ')
    word_i = change[0] - 1
    end_i = -len(change[1]) or len(words[word_i])
    words[word_i] = words[word_i][:end_i] + change[2]
    return ' '.join(words)

if __name__ == '__main__':
    old = open(sys.argv[1]).read()
    for r in repls:
        old = re.sub(r[0], r[1], old)

    lines = old.split('\n')
    for aid, changes in json.load(open('scripts/pause-mark-changes.json')).items():
        for change in changes:
            if lines[int(aid) - 1].startswith('بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِیمِ '):
                change[0] += 4
            lines[int(aid) - 1] = replace_word(lines[int(aid) - 1], change)

    open('quran-uthmani.txt', 'w').write('\n'.join(lines))
