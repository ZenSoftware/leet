/**
 * https://leetcode.com/problems/add-binary/
 */
export { addBinary };

function addBinary(a: string, b: string): string {
  let solution = '';
  let carry = 0;
  let longestLength = Math.max(a.length, b.length);
  let aLastIndex = a.length - 1;
  let bLastIndex = b.length - 1;

  for (let i = 0; i <= longestLength; i++) {
    let aInt = toInt(a[aLastIndex - i]);
    let bInt = toInt(b[bLastIndex - i]);
    let sum = aInt + bInt + carry;

    if (sum > 1) {
      if (sum === 2) solution = '0' + solution;
      else solution = '1' + solution;
      carry = 1;
    } else {
      if (sum === 1) solution = '1' + solution;
      else solution = '0' + solution;
      carry = 0;
    }
  }

  return solution;
}

function toInt(x: string | undefined): number {
  if (x === undefined || x === '0') return 0;
  else return 1;
}
