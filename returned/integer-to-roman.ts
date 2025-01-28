/**
 * https://leetcode.com/problems/integer-to-roman/?envType=study-plan-v2&envId=top-interview-150
 * Given an integer, convert it to a Roman numeral.
 */

export { intToRoman };

function intToRoman(num: number): string {
  let result = '';
  let remainder = num;

  while (remainder > 0) {
    if (remainder - 1000 >= 0) {
      result += 'M';
      remainder -= 1000;
    } else if (remainder - 900 >= 0) {
      result += 'CM';
      remainder -= 900;
    } else if (remainder - 500 >= 0) {
      result += 'D';
      remainder -= 500;
    } else if (remainder - 400 >= 0) {
      result += 'CD';
      remainder -= 400;
    } else if (remainder - 100 >= 0) {
      result += 'C';
      remainder -= 100;
    } else if (remainder - 90 >= 0) {
      result += 'XC';
      remainder -= 90;
    } else if (remainder - 50 >= 0) {
      result += 'L';
      remainder -= 50;
    } else if (remainder - 40 >= 0) {
      result += 'XL';
      remainder -= 40;
    } else if (remainder - 10 >= 0) {
      result += 'X';
      remainder -= 10;
    } else if (remainder - 9 >= 0) {
      result += 'IX';
      remainder -= 9;
    } else if (remainder - 5 >= 0) {
      result += 'V';
      remainder -= 5;
    } else if (remainder - 4 >= 0) {
      result += 'IV';
      remainder -= 4;
    } else if (remainder - 1 >= 0) {
      result += 'I';
      remainder -= 1;
    }
  }

  return result;
}
