// https://leetcode.com/problems/implement-queue-using-stacks/description/
namespace Leet.ImplementQueueUsingStacks;

public class MyQueue
{
    Stack<int> left = new Stack<int>();
    Stack<int> right = new Stack<int>();

    public MyQueue() { }

    public void Push(int x)
    {
        left.Push(x);
    }

    public int Pop()
    {
        if (right.Count > 0)
            return right.Pop();
        else
        {
            while (left.Count > 1)
            {
                right.Push(left.Pop());
            }
            return left.Pop();
        }
    }

    public int Peek()
    {
        if (right.Count > 0)
            return right.Peek();
        else
        {
            while (left.Count > 0)
            {
                right.Push(left.Pop());
            }
            return right.Peek();
        }
    }

    public bool Empty()
    {
        return left.Count == 0 && right.Count == 0;
    }
}
