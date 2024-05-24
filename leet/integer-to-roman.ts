/**
 * https://leetcode.com/problems/integer-to-roman/description/
 */

export function intToRoman(num: number): string {
  const s = num.toString();
  let result = "";

  return result;
}

const ROMAN = {
  I: 1,
  V: 5,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000,
};

const SUBTRACTIVE = {
  4: "IV",
  9: "IX",
  40: "XL",
  90: "XC",
  400: "CD",
  900: "CM",
};
