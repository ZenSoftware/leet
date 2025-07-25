import { longestCommonPrefix } from './longest-common-prefix';

describe('Longest Common Prefix', () => {
  it('evaluates correctly', () => {
    expect(longestCommonPrefix(['flower', 'flow', 'flight'])).toEqual('fl');
    expect(longestCommonPrefix(['dog', 'racecar', 'car'])).toEqual('');
  });
});
