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
        if (a == null && b == null)
            return true;
        if (a == null || b == null || a.val != b.val)
            return false;
        var queue = new Queue<(Node, Node)>();
        queue.Enqueue((a, b));
        var visited = new HashSet<Node> { a };
        while (queue.Count > 0)
        {
            var (curA, curB) = queue.Dequeue();
            if (curA.neighbors.Count != curB.neighbors.Count)
                return false;
            foreach (var adjA in curA.neighbors)
            {
                if (!visited.Contains(adjA))
                {
                    visited.Add(adjA);
                    var adjB = curB.neighbors.Where(x => x.val == adjA.val).FirstOrDefault();
                    if (adjB == null)
                        return false;
                    queue.Enqueue((adjA, adjB));
                }
            }
        }
        return true;
    }
}