import { singleNumber } from './single-number-ii';

describe('Single Number II', () => {
  it('evaluates correctly', () => {
    expect(singleNumber([2, 2, 3, 2])).toEqual(3);
    expect(singleNumber([0, 1, 0, 1, 0, 1, 99])).toEqual(99);
  });
});
