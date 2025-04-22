// https://leetcode.com/problems/basic-calculator/description/
namespace Today2.BasicCalculator;

public class Solution
{
    public int Calculate(string s)
    {
        var stack = new Stack<int>();
        int i = 0, sign = 1, result = 0;

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
                        var num = 0;
                        num += s[i] - '0';
                        while (i + 1 < s.Length && char.IsDigit(s[i + 1]))
                        {
                            i++;
                            num = (10 * num) + s[i] - '0';
                        }
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