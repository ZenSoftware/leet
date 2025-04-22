using Today2.MergeIntervals;
namespace Today2;

internal class MergeIntervalsTest()
{
    [Test]
    public void Test1()
    {
        var solution = new Solution();
        var result = solution.Merge([[1, 3], [2, 6], [8, 10], [15, 18]]);
        int[][] answer = {
            new int[]{ 1, 6 },
            new int[]{ 8, 10 },
            new int[]{ 15, 18 }
        };
        Assert.That(result, Is.EqualTo(answer));
    }

    [Test]
    public void Test2()
    {
        var solution = new Solution();
        var result = solution.Merge([[1, 4], [4, 5]]);
        int[][] answer = {
            new int[]{ 1, 5 }
        };
        Assert.That(result, Is.EqualTo(answer));
    }

    [Test]
    public void Test3()
    {
        var solution = new Solution();
        var result = solution.Merge([[1, 4], [2, 3]]);
        int[][] answer = {
            new int[]{ 1, 4 }
        };
        Assert.That(result, Is.EqualTo(answer));
    }

    [Test]
    public void Test4()
    {
        var solution = new Solution();
        var result = solution.Merge([[1, 4], [0, 2], [3, 5]]);
        int[][] answer = {
            new int[]{ 0, 5 }
        };
        Assert.That(result, Is.EqualTo(answer));
    }

    [Test]
    public void Test5()
    {
        var solution = new Solution();
        var result = solution.Merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]);
        int[][] answer = {
            new int[]{ 1, 10 }
        };
        Assert.That(result, Is.EqualTo(answer));
    }
}