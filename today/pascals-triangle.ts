/**
 * https://leetcode.com/problems/pascals-triangle/
 */
export { generate };

function generate(numRows: number): number[][] {
  if (numRows === 1) return [[1]];

  const result: number[][] = [[1]];
  for (let i = 1; i < numRows; i++) {
    let next: number[] = Array(i + 1);
    result.push(next);
    next[0] = 1;
    next[next.length - 1] = 1;
    for (let j = 1; j < next.length - 1; j++) {
      const lastRow = result[i - 1];
      next[j] = lastRow[j - 1] + lastRow[j];
    }
  }

  return result;
}
