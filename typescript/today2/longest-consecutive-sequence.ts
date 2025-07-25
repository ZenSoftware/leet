/**
 * https://leetcode.com/problems/longest-consecutive-sequence/description/
 */
export { longestConsecutive };

function longestConsecutive(nums: number[]): number {
  const set = new Set(nums);
  let longest = 0;

  for (let n of set) {
    if (!set.has(n - 1)) {
      let j = n + 1;
      while (set.has(j)) {
        j++;
      }
      longest = Math.max(longest, j - n);
    }
  }

  return longest;
}
