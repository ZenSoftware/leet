namespace Leet.TopKFrequentElements
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

            var values = dict.OrderByDescending(kv => kv.Value);
            var result = new int[k];

            for(int i = 0; i<k; i++)
            {
                result[i] = values.ElementAt(i).Key;
            }

            return result;
        }
    }
}
