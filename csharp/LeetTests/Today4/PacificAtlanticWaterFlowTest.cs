using Today4.PacificAtlanticWaterFlow;
namespace Today4;

internal class PacificAtlanticWaterFlowTest
{
    [Test]
    public void Test1()
    {
        var solution = new Solution();
        int[][] heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]];
        var result = solution.PacificAtlantic(heights);
        int[][] answer = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]];
        Assert.That(result, Is.EqualTo(answer));
    }

    [Test]
    public void Test2()
    {
        var solution = new Solution();
        int[][] heights = [[1]];
        var result = solution.PacificAtlantic(heights);
        int[][] answer = [[0, 0]];
        Assert.That(result, Is.EqualTo(answer));
    }
}