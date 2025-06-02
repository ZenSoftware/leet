import { reverseWords } from './reverse-words-in-a-string';

describe('Reverse Words in a String', () => {
  it('evaluates correctly', () => {
    expect(reverseWords('the sky is blue')).toEqual('blue is sky the');
    expect(reverseWords('  hello world  ')).toEqual('world hello');
    expect(reverseWords('a good   example')).toEqual('example good a');
  });
});
