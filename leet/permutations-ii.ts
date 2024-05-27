/**
 * https://leetcode.com/problems/permutations-ii/
 */
export function permuteUnique(nums: number[]): number[][] {
  function permute(elements: number[]) {
    if (elements.length === 0) return [[]];

    const first = elements[0];
    const withoutFirst = elements.slice(1);
    const permsWithoutFirst = permute(withoutFirst);
    const result: number[][] = [];

    for (let perm of permsWithoutFirst) {
      for (let i = 0; i <= perm.length; i++) {
        result.push([...perm.slice(0, i), first, ...perm.slice(i)]);
      }
    }

    return result;
  }

  nums.sort((a, b) => a - b);
  return permute(nums);
}
