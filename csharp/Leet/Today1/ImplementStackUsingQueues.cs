namespace Leet.ImplementStackUsingQueues;

public class MyStack
{
    Queue<int> left = new Queue<int>();
    Queue<int> right = new Queue<int>();

    public MyStack() { }

    public void Push(int x)
    {
        if (left != null)
            left.Enqueue(x);
        else
            right.Enqueue(x);
    }

    public int Pop()
    {
        if (left.Count > 0)
        {
            while (left.Count > 1)
                right.Enqueue(left.Dequeue());
            return left.Dequeue();
        }
        else
        {
            while (right.Count > 1)
                left.Enqueue(right.Dequeue());
            return right.Dequeue();
        }
    }

    public int Top()
    {
        if (left.Count > 0)
        {
            while (left.Count > 1)
                right.Enqueue(left.Dequeue());
            var top = left.Dequeue();
            right.Enqueue(top);
            return top;
        }
        else
        {
            while (right.Count > 1)
                left.Enqueue(right.Dequeue());
            var top = right.Dequeue();
            left.Enqueue(top);
            return top;
        }
    }

    public bool Empty()
    {
        return left.Count == 0 && right.Count == 0;
    }
}
