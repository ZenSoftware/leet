/**
 * https://leetcode.com/problems/add-binary/
 */
export { addBinary };

function addBinary(a: string, b: string): string {
  let carry = 0;
  let longestLength = Math.max(a.length, b.length);
  let solution: string[] = Array(longestLength);
  let aLastIndex = a.length - 1;
  let bLastIndex = b.length - 1;

  for (let i = 0; i < longestLength; i++) {
    let aInt = toInt(a[aLastIndex - i]);
    let bInt = toInt(b[bLastIndex - i]);
    let sum = aInt + bInt + carry;

    if (sum > 1) {
      if (sum === 2) solution[i] = '0';
      else solution[i] = '1';
      carry = 1;
    } else {
      if (sum === 1) solution[i] = '1';
      else solution[i] = '0';
      carry = 0;
    }
  }

  if (carry > 0) solution.push('1');

  return solution.reverse().join('');
}

function toInt(x: string | undefined): number {
  if (x === undefined || x === '0') return 0;
  else return 1;
}
