/**
 * https://leetcode.com/problems/pascals-triangle-ii/description/
 */
export { getRow };

function getRow(rowIndex: number): number[] {
  if (rowIndex === 0) return [1];
  if (rowIndex === 1) return [1, 1];

  let lastRow = [1, 1];
  for (let i = 1; i < rowIndex; i++) {
    const nextRow: number[] = Array(lastRow.length + 1);
    nextRow[0] = 1;
    nextRow[nextRow.length - 1] = 1;

    for (let j = 1; j < nextRow.length - 1; j++) {
      nextRow[j] = lastRow[j - 1] + lastRow[j];
    }

    lastRow = nextRow;
  }

  return lastRow;
}
