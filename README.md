# Quran Text

This Quran text is derived from Tanzil's Uthmani text. Most of the changes are taken from the following two texts:
- [The QPC's text (v13)](https://fonts.qurancomplex.gov.sa/wp02/wp-content/uploads/2019/11/Hafs-ver13.zip)
- [khaledhosny/quran-data](https://github.com/khaledhosny/quran-data)

The major goals of this text are threefold:
1. Accuracy.
2. Portability. (In that it doesn't depend on a specific font or device. Rather any device with decent Unicode support can render it.)
3. Unicode-compliance.

## Changes

- Use U+06CC (Farsi Yeh) for all Yaa' positions, instead of U+064A (Arabic Yeh) for starting and middle, and U+0649 (Alef Maksura) for final and isolated.
- Use open Tanween (U+08F0, U+08F1, U+08F2) in ikhfaa and idghaam cases, instead of regular Tanween (U+064B, U+064C, U+064D).
- Don't use Tanween before U+06E2 (Small High Meem) (i.e., in iqlaab cases).
- Use U+06E1 (Small High Dotless Head Of Khah) instead of U+0652 (Sukun).
- Use U+06E4 (Small High Madda) instead of U+0653 (Maddah Above).
- Remove spaces before pause marks.
- Use hamzah below when called for.

## The small (dagger) alif

Add tatweel after joining characters. This is to avoid them from being shown on top of the letter.

For non joining characters, we add a hair space (U+200A) so that the alif appears on the line, not above the letter.
We then add a word joiner (U+2060) so that it doesn't cut the word in half when wrapping.

This is, seemingly, the only portable approach.

## Known Issues

(See [this discussion](https://twitter.com/mustafaj0x/status/1166355034545766401))

- There is no Unicode solution for the laam hamzah alif ligature (i.e., لا but with a hamzah in the middle) used in Quranic orthography (e.g. الـٔاخرة).
- The text should use NBSB instead of the hair space hack. Unfortunately, that approach isn't supported in the real world.
