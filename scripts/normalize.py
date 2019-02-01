"""
This normalizes the Quran's text to make it more searchable.

TODO:
- convert تاء to تاء مربوطة in رحمت and similar
- ىٰ[^ۤۖ-ۜ \n] (ىٰ in middle of word)
- spelling of some individual words
"""

import re

keep_sm_alif = ['رحمن', 'إله', 'لكن', 'ذلك', 'أولئك', 'هذا', 'هؤلاء']

repls = [
    # Remove pause marks and similar
    (1, r'۞ | ۩|[ۤۖ-ۣۭٜۜۢ۬\u2060 ]', ''),
    # These two "small zeros" are used to indicate characters
    # that aren't pronounced.
    # TODO: some of the characters before them need to be removed (e.g. وَمَلَإِی۟هِ)
    (1, r'[۟۠]', ''),

    (0, 'ٱ', 'ا'),
    (0, 'ی', 'ي'),

    # E.g. داوود
    (0, 'وُۥ', 'وو'),
    # E.g. إِبۡرَ ٰ⁠هِـۧمَ
    (0, 'ِـۧ', 'ِي'),
    # TODO: یُحۡـِۧیَ • لِّنُحۡـِۧیَ • إِۦلَـٰفِهِمۡ

    (0, 'ـ', ''),

    # Use more common sukoon and tanweens
    (0, 'ۡ', 'ْ'),
    (0, 'ࣰ', 'ً'),
    (0, 'ࣱ', 'ٌ'),
    (0, 'ࣲ', 'ٍ'),

    (0, 'َٔا', 'آ'),
    # TODO: [ٕٔ]

    (0, 'وٕ', 'ؤ'),
    (0, 'ىٕ', 'ئ'),

    # Small alif
    (0, 'وٰ', 'ا'),
    (0, 'ٰ', 'ا'),  # TODO: revert in keep_sm_alif cases
]

line_repls = {
    2442: [
        (0, 'یَبۡنَؤُمَّ', ''),  # TODO
    ],
    2571: [
        (0, 'ۨ', 'ن'),  # ننجي
    ],
    5463: [
        (0, 'وَأَلَّوِ', ''),  # TODO
    ],
}

def apply_repls(text, repls):
    for r in repls:
        text = re.sub(r[1], r[2], text) if r[0] else text.replace(r[1], r[2])
    return text

text = open('quran-uthmani.txt').read()
text = apply_repls(text, repls)

lines = text.split('\n')
for line_no in line_repls:
    lines[line_no - 1] = apply_repls(lines[line_no - 1], line_repls[line_no])

open('quran-normed.txt', 'w').write('\n'.join(lines))
