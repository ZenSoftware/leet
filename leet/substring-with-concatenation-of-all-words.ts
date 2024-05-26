/**
 * https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
 */
export function findSubstring(s: string, words: string[]): number[] {
  return [];
}

export function permutations(words: string[]): string[][] {
  if (words.length === 0) return [[]];

  const first = words[0];
  const withoutFirst = words.slice(1);
  const permsWithoutFirst = permutations(withoutFirst);
  const result: string[][] = [];

  for (let perm of permsWithoutFirst) {
    for (let i = 0; i <= perm.length; i++) {
      result.push([...perm.slice(0, i), first, ...perm.slice(i)]);
    }
  }

  return result;
}
