/**
 * https://leetcode.com/problems/candy/?envType=study-plan-v2&envId=top-interview-150
 * There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
 * You are giving candies to these children subjected to the following requirements:
 * Each child must have at least one candy.
 * Children with a higher rating get more candies than their neighbors.
 * Return the minimum number of candies you need to have to distribute the candies to the children.
 */

export { candy };

function candy(ratings: number[]): number {
  let result = new Array(ratings.length).fill(1);

  for (let i = 1; i < ratings.length; i++) {
    if (ratings[i - 1] < ratings[i]) {
      result[i] = result[i - 1] + 1;
    }
  }

  for (let i = ratings.length - 2; i >= 0; i--) {
    if (ratings[i] > ratings[i + 1] && result[i] <= result[i + 1]) {
      result[i] = result[i + 1] + 1;
    }
  }

  return result.reduce((prev, cur) => prev + cur);
}
