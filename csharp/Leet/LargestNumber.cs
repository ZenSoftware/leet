// https://leetcode.com/problems/largest-number/
namespace Leet.LargestNumber
{
    public class Solution
    {
        public string LargestNumber(int[] nums)
        {
            var numStrings = new string[nums.Length];
            for (var i = 0; i < nums.Length; i++)
            {
                numStrings[i] = nums[i].ToString();
            }
            var numsString = numStrings.OrderDescending();

            var result = "";
            foreach (var s in numsString)
            {
                result += s;
            }
            return result;
        }
    }
}
