namespace Leet.RepeatedDnaSequences
{
    public class Solution
    {
        public IList<string> FindRepeatedDnaSequences(string s)
        {
            var set = new HashSet<string>();

            for (int i = 0; i < s.Length - 10; i++)
            {
                var a = s[i..(i + 10)];
                for (int j = i + 1; j <= s.Length - 10; j++)
                {
                    var b = s[j..(j + 10)];
                    if (a == b) set.Add(b);
                }
            }

            return set.ToList();
        }
    }
}
