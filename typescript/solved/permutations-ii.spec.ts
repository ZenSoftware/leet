import { permuteUnique } from './permutations-ii';

describe('Permutations II', () => {
  it('evaluates correctly', () => {
    const result = permuteUnique([1, 1, 2]);
    expect(result).toEqual([
      [1, 1, 2],
      [1, 2, 1],
      [2, 1, 1],
    ]);
  });
});
