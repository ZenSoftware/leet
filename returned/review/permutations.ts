function permutations(elements: number[]): number[][] {
  if (elements.length === 0) return [[]];

  const firstEl = elements[0];
  const withoutFirst = elements.slice(1);
  const permsWithoutFirst = permutations(withoutFirst);
  const permsWithFirst: number[][] = [];

  for (let perm of permsWithoutFirst) {
    for (let i = 0; i <= perm.length; i++) {
      const permWithFirst = [...perm.slice(0, i), firstEl, ...perm.slice(i)];
      permsWithFirst.push(permWithFirst);
    }
  }

  return permsWithFirst;
}

console.log(permutations([1, 2, 3]));
