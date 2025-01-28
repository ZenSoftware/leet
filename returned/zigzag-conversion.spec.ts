import { convert } from './zigzag-conversion';

describe('Zigzag Conversion', () => {
  it('evaluates correctly', () => {
    // expect(convert('PAYPALISHIRING', 3)).toEqual('PAHNAPLSIIGYIR');
    // expect(convert('PAYPALISHIRING', 4)).toEqual('PINALSIGYAHRPI');
    expect(convert('AB', 1)).toEqual('AB');
  });
});
