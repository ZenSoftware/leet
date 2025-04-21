using Leet.ImplementStackUsingQueues;

namespace LeetTests;

internal class MyStackTests
{
    [Test]
    public void TestsMyStack()
    {
        MyStack myStack = new MyStack();
        myStack.Push(1);
        myStack.Push(2);
        Assert.That(myStack.Top(), Is.EqualTo(2)); // return 2
        Assert.That(myStack.Pop(), Is.EqualTo(2)); // return 2
        Assert.That(myStack.Empty(), Is.EqualTo(false)); // return False
    }

    [Test]
    public void TestsMyStack2()
    {
        // ["MyStack","push","push","pop","top"]
        // [    [],     [1],   [2],   [],   []]
        MyStack myStack = new MyStack();
        myStack.Push(1);
        myStack.Push(2);
        Assert.That(myStack.Pop(), Is.EqualTo(2));
        Assert.That(myStack.Top(), Is.EqualTo(1));
        Assert.That(myStack.Empty(), Is.EqualTo(false));
    }
}
