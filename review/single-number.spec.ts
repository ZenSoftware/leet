import { singleNumber } from './single-number';

describe('Single Number', () => {
  it('evaluates correctly', () => {
    expect(singleNumber([2, 2, 1])).toEqual(1);
  });
});
