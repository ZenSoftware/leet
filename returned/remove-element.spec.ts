import { removeElement } from './remove-element';

describe('Remove Element', () => {
  it('evaluates correctly', () => {
    let nums = [3, 2, 2, 3];
    let k = removeElement(nums, 3);
    expect(nums).toEqual([2, 2, 2, 3]);
    expect(k).toEqual(2);
  });
});
