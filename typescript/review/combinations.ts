function combinations(elements: number[]): number[][] {
  if (elements.length === 0) return [[]];

  const firstEl = elements[0];
  const withoutFirst = elements.slice(1);
  const combsWithoutFirst = combinations(withoutFirst);
  const combsWithFirst: number[][] = [];

  for (let comb of combsWithoutFirst) {
    combsWithFirst.push([firstEl, ...comb]);
  }

  return [...combsWithoutFirst, ...combsWithFirst];
}

console.log(combinations([1, 2, 3]));
