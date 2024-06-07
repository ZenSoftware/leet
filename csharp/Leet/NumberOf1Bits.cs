// https://leetcode.com/problems/number-of-1-bits/description/
namespace Leet.NumberOf1Bits
{
    public class Solution
    {
        public int HammingWeight(int n)
        {
            var count = 0;
            for (var i = 0; i < 32; i++)
            {
                var firstBit = (n >> i) & 1;
                if (firstBit == 1) count++;
            }
            return count;
        }
    }
}
