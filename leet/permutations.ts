/**
 * https://leetcode.com/problems/permutations/description/
 */
export function permute(nums: number[]): number[][] {
  if (nums.length === 0) return [[]];

  const first = nums[0];
  const withoutFirst = nums.slice(1);
  const permsWithoutFirst = permute(withoutFirst);
  const result: number[][] = [];

  for (let perm of permsWithoutFirst) {
    for (let i = 0; i <= perm.length; i++) {
      result.push([...perm.slice(0, i), first, ...perm.slice(i)]);
    }
  }

  return result;
}
