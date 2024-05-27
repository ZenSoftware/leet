/**
 * https://leetcode.com/problems/permutations-ii/
 */
export function permuteUnique(nums: number[]): number[][] {
  let results: number[][] = [];

  let counter: { [key: number]: number } = {};
  for (let num of nums) {
    if (!(num in counter)) counter[num] = 0;
    counter[num]++;
  }

  const backtrack = (comb: number[]) => {
    if (comb.length === nums.length) {
      results.push([...comb]);
      return;
    }

    for (let num in counter) {
      if (counter[num] === 0) continue;

      comb.push(parseInt(num));
      counter[num]--;
      backtrack(comb);
      comb.pop();
      counter[num]++;
    }
  };

  backtrack([]);
  return results;
}
