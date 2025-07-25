import { maxProduct } from './maximum-product-subarray';

describe('Maximum Product Subarray', () => {
  it('evaluates correctly', () => {
    expect(maxProduct([2, 3, -2, 4])).toEqual(6);
    expect(maxProduct([-2, 0, -1])).toEqual(0);
    expect(maxProduct([99])).toEqual(99);
    expect(maxProduct([0, 2])).toEqual(2);
  });
});
