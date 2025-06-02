import { rotate } from './rotate-array';

describe('Rotate Array', () => {
  it('evaluates correctly 1', () => {
    const nums = [1, 2, 3, 4, 5, 6, 7];
    rotate(nums, 3);
    expect(nums).toEqual([5, 6, 7, 1, 2, 3, 4]);
  });
  it('evaluates correctly 2', () => {
    const nums = [-1, -100, 3, 99];
    rotate(nums, 2);
    expect(nums).toEqual([3, 99, -1, -100]);
  });
});
