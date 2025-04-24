using Today4.SerializeAndDeserializeBinaryTree;
namespace Today4;

internal class SerializeAndDeserializeBinaryTreeTest()
{
    [Test]
    public void Test1()
    {
        var codec = new Codec();
        var n1 = new TreeNode(1);
        var n2 = new TreeNode(2);
        var n3 = new TreeNode(3);
        var n4 = new TreeNode(4);
        var n5 = new TreeNode(5);
        n1.left = n2;
        n1.right = n3;
        n3.left = n4;
        n3.right = n5;
        var serialized = codec.serialize(n1);
        Assert.That(serialized, Is.EqualTo("1,2,n,n,3,4,n,n,5"));
        var deserialized = codec.deserialize(serialized);
        Assert.That(IsSameTree(n1, deserialized), Is.EqualTo(true));
    }

    [Test]
    public void Test2()
    {
        var codec = new Codec();
        var serialized = codec.serialize(null);
        Assert.That(serialized, Is.EqualTo(""));
        var deserialized = codec.deserialize(serialized);
        Assert.That(IsSameTree(null, deserialized), Is.EqualTo(true));
    }

    private bool IsSameTree(TreeNode a, TreeNode b)
    {
        if (a == null && b == null)
            return true;
        if (a == null || b == null)
            return false;
        return a.val == b.val && IsSameTree(a.left, b.left) && IsSameTree(a.right, b.right);
    }
}