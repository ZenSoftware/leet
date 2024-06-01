/**
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
 */
export { maxProfit };

function maxProfit(prices: number[]): number {
  let max = 0;

  for (let i = 0; i < prices.length - 1; i++) {
    for (let j = i + 1; j < prices.length; j++) {
      const profit = prices[j] - prices[i];
      if (profit > max) max = profit;
    }
  }

  return max;
}
