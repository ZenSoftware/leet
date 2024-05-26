import { nextPermutation } from './next-permutation';

describe('Next Permutation', () => {
  it('evaluates correctly 1', () => {
    const input = [1, 2, 3];
    nextPermutation(input);
    expect(input).toEqual([1, 3, 2]);
  });

  it('evaluates correctly 2', () => {
    const input = [3, 2, 1];
    nextPermutation(input);
    expect(input).toEqual([1, 2, 3]);
  });

  it('evaluates correctly 3', () => {
    const input = [1, 1, 5];
    nextPermutation(input);
    expect(input).toEqual([1, 5, 1]);
  });
});
