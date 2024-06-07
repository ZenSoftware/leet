// https://leetcode.com/problems/rotate-array/description/
namespace Leet.RotateArray
{
    public class Solution
    {
        public void Rotate(int[] nums, int k)
        {
            k = k % nums.Length;
            var left = nums[..^k];
            var right = nums[(nums.Length - k)..];
            var result = right.Concat(left).ToArray();

            for (var i = 0; i < nums.Length; i++)
            {
                nums[i] = result[i];
            }
        }
    }
}
