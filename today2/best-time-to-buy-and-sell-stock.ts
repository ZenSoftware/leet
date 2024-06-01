/**
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
 */
export { maxProfit };

function maxProfit(prices: number[]): number {
  let left = 0;
  let right = 1;

  for (let i = 0; i < prices.length - 1; i++) {
    if (prices[i + 1] >= prices[right]) right = i + 1;
    if (prices[i] < prices[left] && i < right) left = i;
  }

  return -1;
}
