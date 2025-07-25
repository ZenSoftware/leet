/**
 * https://leetcode.com/problems/group-anagrams/
 */
export function groupAnagrams(strs: string[]): string[][] {
  const grouped: Record<string, string[]> = {};
  for (let s of strs) {
    const sorted = s.split('').sort().join();
    if (!grouped[sorted]) grouped[sorted] = [];
    grouped[sorted].push(s);
  }
  return Object.values(grouped);
}
