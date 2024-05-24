/**
 * https://leetcode.com/problems/zigzag-conversion/
 * The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
 * P   A   H   N
 * A P L S I I G
 * Y   I   R
 * And then read line by line: "PAHNAPLSIIGYIR"
 * Write the code that will take a string and make this conversion given a number of rows:
 * string convert(string s, int numRows);
 */
export function convert(s: string, numRows: number): string {
  const table = new Array(numRows);
  for (let i = 0; i < table.length; i++) {
    table[i] = [];
  }

  let row = 0;
  let col = 0;
  let i = 0;

  while (i < s.length) {
    while (row < numRows && i < s.length) {
      table[row][col] = s[i];
      row++;
      i++;
    }

    row -= 2;

    while (row > 0 && i < s.length) {
      col++;
      table[row][col] = s[i];
      row--;
      i++;
    }

    row = 0;
    col++;
  }

  let result = "";
  for (let row = 0; row < numRows; row++) {
    for (let col = 0; col < table[row].length; col++) {
      const char = table[row][col];
      if (char) result += char;
    }
  }

  return result;
}
