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

        public int[] MergeSort(int[] nums)
        {
            var mid = (Index)Math.Floor(nums.Length / 2d);
            var left = MergeSort(nums[0..mid]);
            var right = MergeSort(nums[mid..]);
            return Merge(left, right);
        }

        public int[] Merge(int[] left, int[] right)
        {
            var result = new int[left.Length + right.Length];
            var i = 0;
            var l = 0;
            var r = 0;
            while (l < left.Length && r < right.Length)
            {
                if (left[l] < right[r])
                    result[i] = left[l++];
                else
                    result[i] = right[r++];
                i++;
            }

            while (l < left.Length)
            {
                result[i] = left[l++];
                i++;
            }

            while (r < right.Length)
            {
                result[i] = right[r++];
                i++;
            }

            return result;
        }
    }
}
