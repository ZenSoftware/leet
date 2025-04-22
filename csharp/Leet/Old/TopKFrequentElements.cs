// https://leetcode.com/problems/top-k-frequent-elements/description/
namespace Old.TopKFrequentElements
{
    public class Solution
    {
        public int[] TopKFrequent(int[] nums, int k)
        {
            var dict = new Dictionary<int, int>();
            foreach (var n in nums)
            {
                if (dict.TryGetValue(n, out var count))
                    dict[n] = count + 1;
                else
                    dict.Add(n, 1);
            }

            var buckets = new List<int>[nums.Length + 1];
            foreach (var (n, count) in dict)
            {
                if (buckets[count] == null) buckets[count] = new List<int>();
                buckets[count].Add(n);
            }

            var i = buckets.Length - 1;
            var result = new int[k];
            var r = 0;
            while (r < k)
            {
                if (buckets[i] != null && buckets[i].Count > 0)
                {
                    foreach (var key in buckets[i])
                    {
                        result[r] = key;
                        r++;
                        if (r >= k) break;
                    }
                }
                i--;
            }

            return result;
        }
    }
}
