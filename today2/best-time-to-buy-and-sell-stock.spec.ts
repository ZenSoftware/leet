import { maxProfit } from './best-time-to-buy-and-sell-stock';

describe('Best Time to Buy and Sell Stock', () => {
  it('evaluates correctly', () => {
    expect(maxProfit([7, 1, 5, 3, 6, 4])).toEqual(5);
    expect(maxProfit([7, 6, 4, 3, 1])).toEqual(0);
    expect(maxProfit([2, 1, 2, 1, 0, 1, 2])).toEqual(2);
    expect(maxProfit([7, 6, 4, 3, 1])).toEqual(0);
    expect(maxProfit([3, 3, 5, 0, 0, 3, 1, 4])).toEqual(4);
  });
});
