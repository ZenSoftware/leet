import { grayCode } from './gray-code';

describe('Gray Code', () => {
  it('evaluates correctly 1', () => {
    expect(grayCode(2)).toEqual([0, 1, 3, 2]);
  });
});
