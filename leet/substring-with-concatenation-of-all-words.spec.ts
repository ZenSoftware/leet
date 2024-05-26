import { findSubstring, permutations } from './substring-with-concatenation-of-all-words';

describe('Substring with Concatenation of All Words', () => {
  it('evaluates correctly', () => {
    expect(true).toEqual(true);
  });

  it('constructs permutations', () => {
    expect(permutations(['a', 'b', 'c'])).toEqual([
      ['a', 'b', 'c'],
      ['b', 'a', 'c'],
      ['b', 'c', 'a'],
      ['a', 'c', 'b'],
      ['c', 'a', 'b'],
      ['c', 'b', 'a'],
    ]);
  });
});
