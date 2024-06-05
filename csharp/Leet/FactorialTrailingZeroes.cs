namespace Leet.FactorialTrailingZeroes
{
    public class Solution
    {
        private Dictionary<long, long> _factorialCache = new Dictionary<long, long>();

        public int TrailingZeroes(int n)
        {
            var factorial = Factorial(n).ToString();
            if (factorial == "0") return 0;

            var count = 0;
            for (var i = factorial.Length - 1; i >= 0; i--)
            {
                if (factorial[i] != '0') break;
                count++;
            }
            return count;
        }

        public long Factorial(long n)
        {
            if (_factorialCache.ContainsKey(n)) return _factorialCache[n];
            if (n == 1) return 1;
            if (n == 0) return 0;
            var result = Factorial(n - 1) * n;
            _factorialCache.Add(n, result);
            return result;
        }
    }
}
