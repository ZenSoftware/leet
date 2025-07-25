/**
 * https://leetcode.com/problems/roman-to-integer/description/
 */
export function romanToInt(s: string): number {
  let i = 0;
  let result = 0;

  while (i < s.length) {
    if (i < s.length - 1) {
      const twoChars = s[i] + s[i + 1];
      const subtractive = SUBTRACTIVE[twoChars];
      if (subtractive !== undefined) {
        result += subtractive;
        i += 2;
        continue;
      }
    }

    const roman = ROMAN[s[i]];
    result += roman;
    i++;
  }

  return result;
}

const ROMAN: Record<string, number> = {
  M: 1000,
  D: 500,
  C: 100,
  L: 50,
  X: 10,
  V: 5,
  I: 1,
};

const SUBTRACTIVE: Record<string, number> = {
  CM: 900,
  CD: 400,
  XC: 90,
  XL: 40,
  IX: 9,
  IV: 4,
};
