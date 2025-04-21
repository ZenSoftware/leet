// https://leetcode.com/problems/min-stack/description/

namespace Leet.MinStack;

public class MinStack
{
    List<(int Value, int Minimum)> stack = new List<(int, int)>();

    public MinStack()
    {
        stack.Add((0, int.MaxValue));
    }

    public void Push(int val)
    {
        var min = Math.Min(val, stack[^1].Minimum);
        stack.Add((val, min));
    }

    public void Pop()
    {
        stack.RemoveAt(stack.Count - 1);
    }

    public int Top()
    {
        return stack[^1].Value;
    }

    public int GetMin()
    {
        return stack[^1].Minimum;
    }
}