/**
 * https://leetcode.com/problems/single-number-ii/description/
 */
export { singleNumber };

function singleNumber(nums: number[]): number {
  let result = 0;

  for (let digitIndex = 0; digitIndex <= 31; digitIndex++) {
    const pow2Num = 1 << digitIndex;
    let digitSum = 0;
    for (let i = 0; i < nums.length; i++) {
      digitSum += (pow2Num & nums[i]) >> digitIndex;
    }
    const setBit = digitSum % 3;
    result += setBit << digitIndex;
  }

  return result;
}
