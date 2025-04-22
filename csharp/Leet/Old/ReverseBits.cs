namespace Old.ReverseBits
{
    public class Solution
    {
        public uint reverseBits(uint n)
        {
            var result = 0u;
            for (var i = 0; i < 32; i++)
            {
                result |= (((1u << i) & n) >> i) << (31 - i);
            }
            return result;
        }
    }
}
