// https://leetcode.com/problems/valid-parentheses/description/

namespace Today1.ValidParentheses;

public class Solution
{
    public bool IsValid(string s)
    {
        var stack = new Stack<char>();
        for (int i = 0; i < s.Length; i++)
        {
            if (s[i] == '(' || s[i] == '{' || s[i] == '[')
                stack.Push(s[i]);
            else
            {
                if (stack.Count == 0)
                    return false;

                var openBraket = stack.Pop();

                if (s[i] == ')')
                {
                    if (openBraket != '(')
                        return false;
                }
                else if (s[i] == '}')
                {
                    if (openBraket != '{')
                        return false;
                }
                else if (s[i] == ']')
                {
                    if (openBraket != '[')
                        return false;
                }
            }
        }
        return stack.Count == 0;
    }
}