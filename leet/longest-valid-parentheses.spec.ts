import { longestValidParentheses, validParentheses } from './longest-valid-parentheses';

describe('Longest Valid Parentheses', () => {
  it('evaluates correctly', () => {
    expect(longestValidParentheses('(()')).toEqual(2);
    expect(longestValidParentheses(')()())')).toEqual(4);
    expect(longestValidParentheses('')).toEqual(0);
  });

  it('evaluates correctly', () => {
    expect(validParentheses('(()())')).toEqual(true);
    expect(validParentheses('(()')).toEqual(false);
    expect(validParentheses('())')).toEqual(false);
    expect(validParentheses('()(')).toEqual(false);
  });
});
