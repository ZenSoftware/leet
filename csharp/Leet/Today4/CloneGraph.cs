// https://leetcode.com/problems/clone-graph/description/
namespace Today4.CloneGraph;

public class Node
{
    public int val;
    public IList<Node> neighbors;

    public Node()
    {
        val = 0;
        neighbors = new List<Node>();
    }

    public Node(int _val)
    {
        val = _val;
        neighbors = new List<Node>();
    }

    public Node(int _val, List<Node> _neighbors)
    {
        val = _val;
        neighbors = _neighbors;
    }
}

public class Solution
{
    public Node CloneGraph(Node node)
    {
        if (node == null)
            return null;

        var nodes = new Dictionary<Node, Node>();
        nodes.Add(node, new Node(node.val));

        var queue = new Queue<Node>();
        queue.Enqueue(node);

        while (queue.Count > 0)
        {
            var cur = queue.Dequeue();
            foreach (var adj in cur.neighbors)
            {
                if (!nodes.Keys.Contains(adj))
                {
                    nodes.Add(adj, new Node(adj.val));
                    queue.Enqueue(adj);
                }
            }
        }

        foreach (var cur in nodes)
        {
            foreach (var adj in cur.Key.neighbors)
            {
                cur.Value.neighbors.Add(nodes[adj]);
            }
        }

        return nodes[node];
    }
}