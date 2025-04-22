using Today1.DesignCircularQueue;

namespace LeetTests.Today1;

internal class DesignCircularQueueTest
{
    [Test]
    public void TestDesignCircularQueue()
    {
        MyCircularQueue myCircularQueue = new MyCircularQueue(3);
        Assert.That(myCircularQueue.EnQueue(1), Is.EqualTo(true));  // return True
        Assert.That(myCircularQueue.EnQueue(2), Is.EqualTo(true));  // return True
        Assert.That(myCircularQueue.EnQueue(3), Is.EqualTo(true));  // return True
        Assert.That(myCircularQueue.EnQueue(4), Is.EqualTo(false)); // return False
        Assert.That(myCircularQueue.Rear(), Is.EqualTo(3));         // return 3
        Assert.That(myCircularQueue.IsFull(), Is.EqualTo(true));    // return True
        Assert.That(myCircularQueue.DeQueue(), Is.EqualTo(true));   // return True
        Assert.That(myCircularQueue.EnQueue(4), Is.EqualTo(true));  // return True
        Assert.That(myCircularQueue.Rear(), Is.EqualTo(4));         // return 4
    }
}
