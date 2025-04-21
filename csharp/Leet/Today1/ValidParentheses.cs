// https://leetcode.com/problems/valid-parentheses/description/

namespace Leet.ValidParentheses;

public class Solution
{
    public bool IsValid(string s)
    {
        var stack = new List<char>();
        for (int i = 0; i < s.Length; i++)
        {
            if (s[i] == '(' || s[i] == '{' || s[i] == '[')
                stack.Add(s[i]);
            else
            {
                if (stack.Count == 0)
                    return false;

                var openBraket = stack[stack.Count - 1];

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

                stack.RemoveAt(stack.Count - 1);
            }
        }
        return stack.Count == 0;
    }
}