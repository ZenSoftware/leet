import { productExceptSelf } from './product-of-array-except-self';

describe('Product of Array Except Self', () => {
  it('evaluates correctly', () => {
    expect(productExceptSelf([1, 2, 3, 4])).toEqual([24, 12, 8, 6]);
    expect(productExceptSelf([1, 2])).toEqual([2, 1]);
    expect(productExceptSelf([1])).toEqual([1]);
    // expect(productExceptSelf([-1, 1, 0, -3, 3])).toEqual([0, 0, 9, 0, 0]);
  });
});
