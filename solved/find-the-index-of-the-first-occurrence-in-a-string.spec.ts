import { strStr } from './find-the-index-of-the-first-occurrence-in-a-string';

describe('Find the Index of the First Occurrence in a String', () => {
  it('evaluates correctly 1', () => {
    expect(strStr('sadbutsad', 'sad')).toEqual(0);
  });

  it('evaluates correctly 2', () => {
    expect(strStr('leetcode', 'leeto')).toEqual(-1);
  });

  it('evaluates correctly 3', () => {
    expect(strStr('abcd', 'cd')).toEqual(2);
  });

  it('evaluates correctly 4', () => {
    expect(strStr('ab', 'cde')).toEqual(-1);
  });
});
