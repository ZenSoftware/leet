import { convertToTitle } from './excel-sheet-column-title';

describe('Excel Sheet Column Title', () => {
  it('evaluates correctly', () => {
    expect(convertToTitle(1)).toEqual('A');
    expect(convertToTitle(28)).toEqual('AB');
    expect(convertToTitle(701)).toEqual('ZY');
    expect(convertToTitle(52)).toEqual('AZ');
  });
});
