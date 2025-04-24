// https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
using Leet.Tree;
namespace Today4.SerializeAndDeserializeBinaryTree;

public class Codec
{
    // Encodes a tree to a single string.
    public string serialize(TreeNode root)
    {
        if (root == null)
            return "";

        var encoded = new List<string>();

        void DFS(TreeNode root)
        {
            if (root == null)
            {
                encoded.Add("n");
                return;
            }

            encoded.Add(root.val.ToString());
            DFS(root.left);
            DFS(root.right);
        }
        DFS(root);

        var end = encoded.Count - 1;
        while (encoded[end] == "n")
        {
            end--;
        }

        return String.Join(",", encoded[..(end + 1)]);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(string data)
    {
        if (String.IsNullOrEmpty(data))
            return null;

        var values = data.Split(",");
        var i = -1;

        TreeNode DFS()
        {
            i++;
            if (i >= values.Length || values[i] == "n")
                return null;
            var node = new TreeNode(int.Parse(values[i]));
            node.left = DFS();
            node.right = DFS();
            return node;
        }
        return DFS();
    }
}