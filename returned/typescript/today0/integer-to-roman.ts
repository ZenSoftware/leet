/**
 * https://leetcode.com/problems/integer-to-roman/?envType=study-plan-v2&envId=top-interview-150
 * Given an integer, convert it to a Roman numeral.
 */

export { intToRoman };

function intToRoman(num: number): string {
  const values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
  const roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'];
  let result = '';
  let remainder = num;

  while (remainder > 0) {
    for (let i = 0; i < roman.length; i++) {
      if (remainder - values[i] >= 0) {
        result += roman[i];
        remainder -= values[i];
        break;
      }
    }
  }

  return result;
}
