/**
 * https://leetcode.com/problems/zigzag-conversion/?envType=study-plan-v2&envId=top-interview-150
 * The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
 * P   A   H   N
 * A P L S I I G
 * Y   I   R
 * And then read line by line: "PAHNAPLSIIGYIR"
 * Write the code that will take a string and make this conversion given a number of rows:
 */

export { convert };

function convert(s: string, numRows: number): string {
  if (numRows === 1) return s;

  let result = new Array(numRows).fill('');

  let i = 0;
  let n = 0;
  let ascending = true;

  while (i < s.length) {
    result[n] += s[i];

    if (ascending) {
      if (n === numRows - 1) {
        ascending = false;
        n--;
      } else {
        n++;
      }
    } else {
      if (n === 0) {
        ascending = true;
        n++;
      } else {
        n--;
      }
    }

    i++;
  }

  return result.join('');
}
