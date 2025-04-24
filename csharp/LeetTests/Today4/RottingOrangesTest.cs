using Today4.RottingOranges;
namespace Today4;

internal class RottingOrangesTest()
{
    [Test]
    public void Test1()
    {
        var solution = new Solution();
        var result = solution.OrangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]);
        Assert.That(result, Is.EqualTo(4));
    }

    [Test]
    public void Test2()
    {
        var solution = new Solution();
        var result = solution.OrangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]);
        Assert.That(result, Is.EqualTo(-1));
    }

    [Test]
    public void Test3()
    {
        var solution = new Solution();
        var result = solution.OrangesRotting([[0, 2]]);
        Assert.That(result, Is.EqualTo(0));
    }
}