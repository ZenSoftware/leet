// https://leetcode.com/problems/min-stack/description/

namespace Today1.MinStack;

public class MinStack
{
    Stack<(int Value, int Minimum)> stack = new Stack<(int, int)>();

    public MinStack()
    {
        stack.Push((0, int.MaxValue));
    }

    public void Push(int val)
    {
        var min = Math.Min(val, stack.Peek().Minimum);
        stack.Push((val, min));
    }

    public void Pop()
    {
        stack.Pop();
    }

    public int Top()
    {
        return stack.Peek().Value;
    }

    public int GetMin()
    {
        return stack.Peek().Minimum;
    }
}