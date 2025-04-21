// https://leetcode.com/problems/design-circular-queue/description/
namespace Leet.DesignCircularQueue;

public class MyCircularQueue
{
    int capacity;
    int[] elements;
    int start = 0;
    int end = -1;
    int count = 0;

    public MyCircularQueue(int k)
    {
        capacity = k;
        elements = new int[k];
    }

    public bool EnQueue(int value)
    {
        if (count == capacity)
            return false;
        end = (end + 1) % capacity;
        elements[end] = value;
        count++;
        return true;
    }

    public bool DeQueue()
    {
        if (count == 0)
            return false;
        start = (start + 1) % capacity;
        count--;
        return true;
    }

    public int Front()
    {
        if (count == 0)
            return -1;
        return elements[start];
    }

    public int Rear()
    {
        if (count == 0)
            return -1;
        return elements[end];
    }

    public bool IsEmpty()
    {
        return count == 0;
    }

    public bool IsFull()
    {
        return count == capacity;
    }
}
