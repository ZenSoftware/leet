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
            numStrings = MergeSort(numStrings);

            var result = "";
            foreach (var s in numStrings)
            {
                result += s;
            }
            return result;
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
            // if (a <= b)
            int iA = 0, iB = 0;
            while (iA != a.Length - 1 || iB != b.Length - 1)
            {
                if (a[iA].CompareTo(b[iB]) < 0)
                    return true;
                else if (a[iA].CompareTo(b[iB]) > 0)
                    return false;

                if (iA < a.Length - 1) iA++;
                if (iB < b.Length - 1) iB++;
            }

            if (a[iA].CompareTo(b[iB]) < 0)
                return true;
            else if (a[iA].CompareTo(b[iB]) > 0)
                return false;

            return true;
        }
    }
}
