// https://leetcode.com/problems/repeated-dna-sequences/description/
namespace Leet.RepeatedDnaSequences
{
    public class Solution
    {
        public IList<string> FindRepeatedDnaSequences(string s)
        {
            var dict = new Dictionary<string, int>();

            for (var i = 0; i < s.Length - 9; i++)
            {
                var seq = s.Substring(i, 10);
                if (!dict.ContainsKey(seq)) dict.Add(seq, 1);
                else dict[seq]++;
            }

            var result = new List<string>();
            foreach (var (seq, count) in dict)
            {
                if (count > 1) result.Add(seq);
            }
            return result;
        }
    }
}
