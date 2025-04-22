using Today2.InsertInterval;
namespace Today2;

internal class InsertIntervalTest()
{
    [Test]
    public void Test1()
    {
        var solution = new Solution();
        var result = solution.Insert([[1, 3], [6, 9]], [2, 5]);
        int[][] answer = [[1, 5], [6, 9]];
        Assert.That(result, Is.EqualTo(answer));
    }

    [Test]
    public void Test2()
    {
        var solution = new Solution();
        var result = solution.Insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]);
        int[][] answer = [[1, 2], [3, 10], [12, 16]];
        Assert.That(result, Is.EqualTo(answer));
    }
}