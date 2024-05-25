/**
 * [Coderbyte - How to Code Combinations Using Recursion](https://www.youtube.com/watch?v=NA2Oj9xqaZQ)
 * Time: O(2^n)
 * Space: O(n^2)
 */
function combinations(elements: any[]): any[][] {
  if (elements.length === 0) return [[]];

  const firstEl = elements[0];
  const withoutFirst = elements.slice(1);
  const combsWithoutFirst = combinations(withoutFirst);
  const combsWithFirst: any[] = [];

  for (let comb of combsWithoutFirst) {
    combsWithFirst.push([firstEl, ...comb]);
  }

  return [...combsWithFirst, ...combsWithoutFirst];
}

console.log(combinations(['a', 'b', 'c']));
