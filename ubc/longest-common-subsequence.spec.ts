import { longestCommonSubsequence } from './longest-common-subsequence';

describe('Longest Common Subsequence', () => {
  it('evaluates correctly 1', () => {
    expect(longestCommonSubsequence('abcde', 'ace')).toEqual(3);
  });

  it('evaluates correctly 2', () => {
    expect(longestCommonSubsequence('abc', 'abc')).toEqual(3);
  });

  it('evaluates correctly 3', () => {
    expect(longestCommonSubsequence('abc', 'def')).toEqual(0);
  });
});
