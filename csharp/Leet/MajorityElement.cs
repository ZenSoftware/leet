namespace Leet.MajorityElement
{
    public class Solution
    {
        public int MajorityElement(int[] nums)
        {
            var count = 0;
            var element = nums[0];

            foreach (var n in nums)
            {
                if (element == n)
                {
                    count++;
                }
                else
                {
                    count--;
                    if (count < 0)
                    {
                        element = n;
                        count = 1;
                    }
                }
            }

            return element;
        }
    }
}
