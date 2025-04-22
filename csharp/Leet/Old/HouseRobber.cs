// https://leetcode.com/problems/house-robber/description/
// NeetCode solution: https://www.youtube.com/watch?v=73r3KWiEvyk

namespace Old.HouseRobber
{
    public class Solution
    {
        public int Rob(int[] nums)
        {
            int rob1 = 0, rob2 = 0;
            foreach (int n in nums)
            {
                var temp = Math.Max(n + rob1, rob2);
                rob1 = rob2;
                rob2 = temp;
            }
            return rob2;
        }

    }
}
