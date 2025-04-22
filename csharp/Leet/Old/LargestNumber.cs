// https://leetcode.com/problems/largest-number/
namespace Old.LargestNumber
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
            numStrings = MergeSort(numStrings);

            var result = "";
            foreach (var s in numStrings)
            {
                result += s;
            }

            var leadingZeroIndex = 0;
            for (var i = 0; i < result.Length - 1; i++)
            {
                if (result[i] == '0') leadingZeroIndex = i + 1;
                else break;
            }

            return result[leadingZeroIndex..];
        }

        public string[] MergeSort(string[] nums)
        {
            if (nums.Length == 1) return nums;
            var mid = (Index)Math.Floor(nums.Length / 2d);
            var left = MergeSort(nums[0..mid]);
            var right = MergeSort(nums[mid..]);
            return Merge(left, right);
        }

        public string[] Merge(string[] left, string[] right)
        {
            var result = new string[left.Length + right.Length];
            int i = 0, l = 0, r = 0;

            while (l < left.Length && r < right.Length)
            {
                if (CompareStrings(left[l], right[r]))
                    result[i] = right[r++];
                else
                    result[i] = left[l++];
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

        public bool CompareStrings(string a, string b)
        {
            var ab = a + b;
            var ba = b + a;
            for (var i = 0; i < a.Length + b.Length; i++)
            {
                var compared = ab[i].CompareTo(ba[i]);
                if (compared < 0) return true;
                else if (compared > 0) return false;
            }
            return true;
        }
    }
}
