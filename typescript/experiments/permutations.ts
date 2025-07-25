/**
 * [Coderbyte - What are Permutations & how do they differ from Combinations?](https://www.youtube.com/watch?v=us0cYQXQpxg)
 * Time: O(n!)
 * Space: O(n^2)
 */
function permutations(elements: any[]): any[][] {
  if (elements.length === 0) return [[]];

  const firstEl = elements[0];
  const withoutFirst = elements.slice(1);
  const permsWithoutFirst = permutations(withoutFirst);
  const results: any[][] = [];

  for (let perm of permsWithoutFirst) {
    for (let i = 0; i <= perm.length; i++) {
      const withFirst = [...perm.slice(0, i), firstEl, ...perm.slice(i)];
      results.push(withFirst);
    }
  }

  return results;
}

console.log(permutations(['a', 'b', 'c']));
