/**
 * https://leetcode.com/problems/pascals-triangle-ii/description/
 */
export { getRow };

function getRow(rowIndex: number): number[] {
  if (rowIndex === 0) return [1];
  if (rowIndex === 1) return [1, 1];

  let lastRow = [1, 1];
  for (let i = 1; i < rowIndex; i++) {
    const newRow: number[] = Array(lastRow.length + 1);
    newRow[0] = 1;
    newRow[newRow.length - 1] = 1;

    for (let j = 1; j < lastRow.length; j++) {
      newRow[j] = lastRow[j - 1] + lastRow[j];
    }

    lastRow = newRow;
  }

  return lastRow;
}
