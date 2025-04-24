using Today4.CloneGraph;
namespace Today4;

internal class CloneGraphTest()
{
    [Test]
    public void Test1()
    {
        var solution = new Solution();
        var n1 = new Node(1);
        var n2 = new Node(2);
        var n3 = new Node(3);
        var n4 = new Node(4);
        n1.neighbors = [n2, n4];
        n2.neighbors = [n1, n3];
        n3.neighbors = [n2, n4];
        n4.neighbors = [n1, n3];
        var result = solution.CloneGraph(n1);
        Assert.That(IsClone(n1, result), Is.EqualTo(true));
    }

    private bool IsClone(Node a, Node b)
    {
        return false;
    }
}