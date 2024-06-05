namespace Leet.FindPeakElement
{
    public class Solution
    {
        public int FindPeakElement(int[] nums)
        {
            if (nums.Length == 1) return 0;
            if (nums.Length == 2)
            {
                if (nums[0] > nums[1]) return 0;
                else return 1;
            }
            return BinarySearch(nums, 0, nums.Length - 1);
        }

        private int BinarySearch(int[] nums, int start, int end)
        {
            var mid = (start + end) / 2;
            if (IsPeak(nums, mid)) return mid;
            if (IsAscending(nums, mid)) return BinarySearch(nums, mid + 1, end);
            else return BinarySearch(nums, start, mid - 1);
        }

        private bool IsPeak(int[] nums, int i)
        {
            if (i == 0)
            {
                if (nums[i] > nums[i + 1]) return true;
                return false;
            }

            if (i == nums.Length - 1)
            {
                if (nums[i - 1] < nums[i]) return true;
                return false;
            }

            return nums[i - 1] < nums[i] && nums[i] > nums[i + 1];
        }

        private bool IsAscending(int[] nums, int i)
        {
            if (i == 0 && nums[i] < nums[i + 1]) return true;
            if (i == nums.Length - 1 && nums[i - 1] < nums[i]) return true;
            return nums[i - 1] < nums[i] && nums[i] < nums[i + 1];
        }
    }
}