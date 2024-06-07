// https://leetcode.com/problems/house-robber/description/

namespace Leet.HouseRobber
{
    public class Solution
    {
        public int Rob(int[] nums)
        {
            return Backtrack(nums, new List<int>());
        }

        public int Backtrack(int[] remaining, List<int> path)
        {
            if (remaining.Length == 0)
            {
                var sum = 0;
                foreach (var p in path) sum += p;
                return sum;
            }

            path.Add(remaining[0]);
            var resultWithFirst = Backtrack(remaining.Skip(2).ToArray(), path);
            path.RemoveAt(path.Count - 1);

            var resultWithoutFirst = Backtrack(remaining.Skip(1).ToArray(), path);

            return Math.Max(resultWithFirst, resultWithoutFirst);
        }
    }
}
