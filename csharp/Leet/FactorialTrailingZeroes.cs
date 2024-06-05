namespace Leet.FactorialTrailingZeroes
{
    public class Solution
    {
        public int TrailingZeroes(int n)
        {
            var remaining = n;
            var power = 1;
            var count = 0;
            while (Math.Pow(5, power) <= n)
            {
                count += (int)Math.Floor(remaining / Math.Pow(5, power));
                power++;
            }
            return count;
        }
    }
}
