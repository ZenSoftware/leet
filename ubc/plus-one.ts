/**
 * https://leetcode.com/problems/plus-one/
 */
export { plusOne };

function plusOne(digits: number[]): number[] {
  const solution = Array(digits.length);
  let carry = 0;

  const lastIndex = digits.length - 1;
  for (let i = lastIndex; i >= 0; i--) {
    let sum = digits[i] + carry;

    if (i === lastIndex) sum += 1;

    if (sum >= 10) {
      solution[i] = sum - 10;
      carry = 1;
    } else {
      solution[i] = sum;
      carry = 0;
    }
  }

  if (carry > 0) solution.unshift(1);

  return solution;
}
