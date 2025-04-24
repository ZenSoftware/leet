// https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
using System.Text;
using Leet.Tree;
namespace Today4.SerializeAndDeserializeBinaryTree;

public class Codec
{
    // Encodes a tree to a single string.
    public string serialize(TreeNode root)
    {
        var result = new List<string>();
        void DFS(TreeNode root)
        {
            if (root == null)
            {
                result.Add("n");
                return;
            }

            result.Add(root.val.ToString());
            DFS(root.left);
            DFS(root.right);
        }
        DFS(root);

        var end = result.Count - 1;
        while (result[end] == "n")
        {
            end--;
        }
        return String.Join(",", result[..(end + 1)]);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(string data)
    {
        var split = data.Split(",");
        var i = -1;
        TreeNode DFS()
        {
            i++;
            if (i >= split.Length || split[i] == "n")
                return null;
            var node = new TreeNode(int.Parse(split[i]));
            node.left = DFS();
            node.right = DFS();
            return node;
        }
        return DFS();
    }
}