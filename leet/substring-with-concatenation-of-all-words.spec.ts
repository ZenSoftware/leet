import {
  findSubstring,
  permutations,
  dedupeWords,
} from './substring-with-concatenation-of-all-words';

describe('Substring with Concatenation of All Words', () => {
  it('evaluates correctly 1', () => {
    expect(findSubstring('barfoothefoobarman', ['foo', 'bar'])).toEqual([0, 9]);
  });

  it('evaluates correctly 2', () => {
    expect(findSubstring('wordgoodgoodgoodbestword', ['word', 'good', 'best', 'good'])).toEqual([]);
  });

  it('deduplicates words', () => {
    expect(dedupeWords(['aa', 'bb', 'cc', 'aa', 'bb'])).toEqual(['aa', 'bb', 'cc']);
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
