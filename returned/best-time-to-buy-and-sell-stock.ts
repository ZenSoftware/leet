/**
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150
 * You are given an array prices where prices[i] is the price of a given stock on the ith day.
 * You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
 * Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
 */

export { maxProfit };

function maxProfit(prices: number[]): number {
  let buyDay = 0;
  let max = 0;
  for (let sellDay = 1; sellDay < prices.length; sellDay++) {
    let profit = prices[sellDay] - prices[buyDay];
    max = Math.max(max, profit);
    if (prices[sellDay] < prices[buyDay]) buyDay = sellDay;
  }
  return max;
}
