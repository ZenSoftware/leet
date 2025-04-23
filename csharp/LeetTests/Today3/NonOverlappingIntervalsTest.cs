using Today3.NonOverlappingIntervals;
namespace Today3;

internal class NonOverlappingIntervalsTest()
{
    [Test]
    public void Test1()
    {
        var solution = new Solution();
        var result = solution.EraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]);
        Assert.That(result, Is.EqualTo(1));
    }

    [Test]
    public void Test2()
    {
        var solution = new Solution();
        var result = solution.EraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]);
        Assert.That(result, Is.EqualTo(2));
    }

    [Test]
    public void Test3()
    {
        var solution = new Solution();
        var result = solution.EraseOverlapIntervals([[1, 2], [2, 3]]);
        Assert.That(result, Is.EqualTo(0));
    }
}