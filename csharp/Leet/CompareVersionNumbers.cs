// https://leetcode.com/problems/compare-version-numbers/
namespace Leet.CompareVersionNumbers
{
    public class Solution
    {
        public int CompareVersion(string version1, string version2)
        {
            var split1 = version1.Split('.');
            var split2 = version2.Split('.');

            var i = 0;
            var j = 0;
            while(i < split1.Length || j < split2.Length)
            {
                var v1 = 0;
                if (i < split1.Length)
                {
                    v1 = Int32.Parse(split1[i]);
                    i++;
                }

                var v2 = 0;
                if (j < split2.Length)
                {
                    v2 = Int32.Parse(split2[j]);
                    j++;
                }

                if (v1 < v2) return -1;
                else if (v1 > v2) return 1;
            }

            return 0;
        }
    }
}
