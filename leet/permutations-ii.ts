/**
 * https://leetcode.com/problems/permutations-ii/
 */
export function permuteUnique(nums: number[]): number[][] {
  let results: number[][] = [];

  let counter: Record<string, number> = {};
  for (let num of nums) {
    if (!(num in counter)) counter[num] = 0;
    counter[num]++;
  }

  function perm(elements: number[]) {
    if (elements.length === nums.length) {
      results.push([...elements]);
      return;
    }

    for (let num in counter) {
      if (counter[num] === 0) continue;

      elements.push(parseInt(num));
      counter[num]--;
      perm(elements);
      elements.pop();
      counter[num]++;
    }
  }

  perm([]);
  return results;
}
