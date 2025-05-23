namespace Today1;

internal class MinStackTest
{
    [Test]
    public void TestMinStack()
    {
        var minStack = new MinStack();
        minStack.Push(-2);
        minStack.Push(0);
        minStack.Push(-3);
        Assert.That(minStack.GetMin(), Is.EqualTo(-3)); // return -3
        minStack.Pop();
        Assert.That(minStack.Top(), Is.EqualTo(0));  // return 0
        Assert.That(minStack.GetMin(), Is.EqualTo(-2)); // return -2
    }
}