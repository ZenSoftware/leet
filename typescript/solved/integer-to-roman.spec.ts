import { intToRoman } from './integer-to-roman';

describe('Integer to Roman', () => {
  it('evaluates correctly', () => {
    expect(intToRoman(3749)).toEqual('MMMDCCXLIX');
    expect(intToRoman(58)).toEqual('LVIII');
    expect(intToRoman(1994)).toEqual('MCMXCIV');
  });
});
