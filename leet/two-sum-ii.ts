/**
 * https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
 */
export function twoSum(numbers: number[], target: number): number[] {
  let result: number[] = [];

  for (let i = 0; i < numbers.length; i++) {
    const find = target - numbers[i];
    const foundIndex = binarySearch(numbers, find, i);
    if (foundIndex !== -1) {
      if (i < foundIndex) {
        return [i + 1, foundIndex + 1];
      } else {
        return [foundIndex + 1, i + 1];
      }
    }
  }

  return result;
}

export function binarySearch(
  numbers: number[],
  find: number,
  excludeIndex: number
) {
  function bs(start: number, end: number) {
    if (excludeIndex !== start && numbers[start] === find) return start;
    if (excludeIndex !== end && numbers[end] === find) return end;
    if (start >= end) return -1;

    const mid = Math.floor((start + end) / 2);

    if (find <= numbers[mid]) return bs(start, mid);
    else return bs(mid + 1, end);
  }

  return bs(0, numbers.length - 1);
}
