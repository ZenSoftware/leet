import { fullJustify, lineCharCount, spaces } from './text-justification';

describe('Text Justification', () => {
  it('evaluates correctly 1', () => {
    const input = ['This', 'is', 'an', 'example', 'of', 'text', 'justification.'];
    expect(fullJustify(input, 16)).toEqual([
      'This    is    an',
      'example  of text',
      'justification.  ',
    ]);
  });

  it('evaluates correctly 2', () => {
    const input = ['What', 'must', 'be', 'acknowledgment', 'shall', 'be'];
    expect(fullJustify(input, 16)).toEqual([
      'What   must   be',
      'acknowledgment  ',
      'shall be        ',
    ]);
  });

  it('evaluates correctly 3', () => {
    const input = [
      'Science',
      'is',
      'what',
      'we',
      'understand',
      'well',
      'enough',
      'to',
      'explain',
      'to',
      'a',
      'computer.',
      'Art',
      'is',
      'everything',
      'else',
      'we',
      'do',
    ];
    expect(fullJustify(input, 20)).toEqual([
      'Science  is  what we',
      'understand      well',
      'enough to explain to',
      'a  computer.  Art is',
      'everything  else  we',
      'do                  ',
    ]);
  });

  it('evaluates character count', () => {
    expect(lineCharCount(['123', '45', '6789'])).toEqual(9);
    expect(lineCharCount([])).toEqual(0);
  });

  it('evaluates get spaces', () => {
    expect(spaces(0)).toEqual('');
    expect(spaces(1)).toEqual(' ');
    expect(spaces(2)).toEqual('  ');
  });
});
