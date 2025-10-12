import { permute } from './permutations';

describe('Permutations', () => {
  it('evaluates correctly', () => {
    const result = permute([1, 2, 3]);
    expect(permute([1, 2, 3])).toEqual([
      [1, 2, 3],
      [2, 1, 3],
      [2, 3, 1],
      [1, 3, 2],
      [3, 1, 2],
      [3, 2, 1],
    ]);
  });
});
