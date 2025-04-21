// https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

namespace Leet.EvaluateReversePolishNotation;

public class Solution
{
    public int EvalRPN(string[] tokens)
    {
        var stack = new List<int>();

        foreach (var token in tokens)
        {
            if (token == "+" || token == "-" || token == "*" || token == "/")
            {
                var y = stack[stack.Count - 1];
                stack.RemoveAt(stack.Count - 1);

                var x = stack[stack.Count - 1];
                stack.RemoveAt(stack.Count - 1);

                switch (token)
                {
                    case "+":
                        stack.Add(x + y);
                        break;
                    case "-":
                        stack.Add(x - y);
                        break;
                    case "*":
                        stack.Add(x * y);
                        break;
                    case "/":
                        stack.Add(x / y);
                        break;
                }
            }
            else
            {
                stack.Add(Int32.Parse(token));
            }
        }
        return stack[0];
    }
}