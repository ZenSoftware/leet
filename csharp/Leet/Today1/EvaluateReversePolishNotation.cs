// https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

namespace Leet.EvaluateReversePolishNotation;

public class Solution
{
    public int EvalRPN(string[] tokens)
    {
        var stack = new Stack<int>();

        foreach (var token in tokens)
        {
            if (token == "+" || token == "-" || token == "*" || token == "/")
            {
                var right = stack.Pop();
                var left = stack.Pop();

                switch (token)
                {
                    case "+":
                        stack.Push(left + right);
                        break;
                    case "-":
                        stack.Push(left - right);
                        break;
                    case "*":
                        stack.Push(left * right);
                        break;
                    case "/":
                        stack.Push(left / right);
                        break;
                }
            }
            else
                stack.Push(Int32.Parse(token));
        }

        return stack.Peek();
    }
}