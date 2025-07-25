/**
 * https://leetcode.com/problems/roman-to-integer/?envType=study-plan-v2&envId=top-interview-150
 * Given a roman numeral, convert it to an integer.
 */

export { romanToInt };

function calcScale(next: string, a: string, b: string): number {
  return next === a || next === b ? -1 : 1;
}

function romanToInt(s: string): number {
  let total = 0;

  for (let i = 0; i < s.length; i++) {
    switch (s[i]) {
      case 'I':
        total += 1 * calcScale(s[i + 1], 'V', 'X');
        break;
      case 'V':
        total += 5;
        break;
      case 'X':
        total += 10 * calcScale(s[i + 1], 'L', 'C');
        break;
      case 'L':
        total += 50;
        break;
      case 'C':
        total += 100 * calcScale(s[i + 1], 'D', 'M');
        break;
      case 'D':
        total += 500;
        break;
      case 'M':
        total += 1000;
        break;
    }
  }

  return total;
}

// I = 1
// V = 5
// X = 10
// L = 50
// C = 100
// D = 500
// M = 1000

// I can be placed before V (5) and X (10) to make 4 and 9.
// X can be placed before L (50) and C (100) to make 40 and 90.
// C can be placed before D (500) and M (1000) to make 400 and 900.
