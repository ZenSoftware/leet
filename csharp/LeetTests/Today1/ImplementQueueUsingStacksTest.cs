using Today1.ImplementQueueUsingStacks;
namespace LeetTests.Today1;

internal class ImplementQueueUsingStacksTest
{
    [Test]
    public void TestImplementQueueUsingStacks()
    {
        MyQueue myQueue = new MyQueue();
        myQueue.Push(1); // queue is: [1]
        myQueue.Push(2); // queue is: [1, 2] (leftmost is front of the queue)
        Assert.That(myQueue.Peek(), Is.EqualTo(1)); // return 1
        Assert.That(myQueue.Pop(), Is.EqualTo(1)); // return 1, queue is [2]
        Assert.That(myQueue.Empty(), Is.EqualTo(false)); // return false
    }

    [Test]
    public void TestImplementQueueUsingStacks2()
    {
        //["MyQueue","push","push","peek","push","peek"]
        //[    [],     [1],   [2],   [],    [3],   []]
        MyQueue myQueue = new MyQueue();
        myQueue.Push(1);
        myQueue.Push(2);
        Assert.That(myQueue.Peek(), Is.EqualTo(1));
        myQueue.Push(3);
        Assert.That(myQueue.Peek(), Is.EqualTo(1));
    }
}