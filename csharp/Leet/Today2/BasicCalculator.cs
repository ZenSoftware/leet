using System.Text;

namespace Today2.BasicCalculator;

public class Solution
{
    public int Calculate(string s)
    {
        var i = 0;
        var sign = 1;
        var stack = new Stack<int>();
        var result = 0;

        while (i < s.Length)
        {
            switch (s[i])
            {
                case ' ':
                    break;
                case '+':
                    sign = 1;
                    break;
                case '-':
                    sign = -1;
                    break;
                case '(':
                    stack.Push(result);
                    stack.Push(sign);
                    result = 0;
                    sign = 1;
                    break;
                case ')':
                    result *= stack.Pop();
                    result += stack.Pop();
                    break;
                default:
                    if (char.IsDigit(s[i]))
                    {
                        var stringBuilder = new StringBuilder();
                        stringBuilder.Append(s[i]);
                        while (i + 1 < s.Length && char.IsDigit(s[i + 1]))
                        {
                            i++;
                            stringBuilder.Append(s[i]);
                        }
                        var num = Int32.Parse(stringBuilder.ToString());
                        num *= sign;
                        result += num;
                    }
                    break;
            }
            i++;
        }
        return result;
    }
}