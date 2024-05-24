/**
 * https://leetcode.com/problems/integer-to-roman/description/
 */

export function intToRoman(num: number): string {
  let result = "";

  while (num > 0) {
    const firstDigit = num.toString()[0];
    if (firstDigit === "4" || firstDigit === "9") {
      for (let [char, val] of Object.entries(SUBTRACTIVE)) {
        if (num >= val) {
          result += char;
          num -= val;
          break;
        }
      }
      continue;
    }

    for (let [char, val] of Object.entries(ROMAN)) {
      if (num >= val) {
        result += char;
        num -= val;
        break;
      }
    }
  }

  return result;
}

const ROMAN = {
  M: 1000,
  D: 500,
  C: 100,
  L: 50,
  X: 10,
  V: 5,
  I: 1,
};

const SUBTRACTIVE = {
  CM: 900,
  CD: 400,
  XC: 90,
  XL: 40,
  IX: 9,
  IV: 4,
};
