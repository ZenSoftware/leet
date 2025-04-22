using Today2.LargestRectangleInHistogram;
namespace Today2;

internal class LargestRectangleInHistogramTest()
{
    [Test]
    public void Test1()
    {
        var solution = new Solution();
        var result = solution.LargestRectangleArea([2, 1, 5, 6, 2, 3]);
        Assert.That(result, Is.EqualTo(10));
    }

    [Test]
    public void Test2()
    {
        var solution = new Solution();
        var result = solution.LargestRectangleArea([2, 4]);
        Assert.That(result, Is.EqualTo(4));
    }
}