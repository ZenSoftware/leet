// https://leetcode.com/problems/implement-queue-using-stacks/description/
namespace Leet.ImplementQueueUsingStacks;

public class MyQueue
{
    List<int> left = new List<int>();
    List<int> right = new List<int>();

    public MyQueue() { }

    public void Push(int x)
    {
        left.Add(x);
    }

    public int Pop()
    {
        if (right.Count > 0)
        {
            var left_pop = right[right.Count - 1];
            right.RemoveAt(right.Count - 1);
            return left_pop;
        }
        else
        {
            while (left.Count > 1)
            {
                var left_pop = left[left.Count - 1];
                left.RemoveAt(left.Count - 1);
                right.Add(left_pop);
            }
            var res = left[0];
            left.RemoveAt(0);
            return res;
        }
    }

    public int Peek()
    {
        if (right.Count > 0)
        {
            return right[^1];
        }
        else
        {
            while (left.Count > 0)
            {
                var left_pop = left[left.Count - 1];
                left.RemoveAt(left.Count - 1);
                right.Add(left_pop);
            }
            return right[^1];
        }
    }

    public bool Empty()
    {
        return left.Count == 0 && right.Count == 0;
    }
}
