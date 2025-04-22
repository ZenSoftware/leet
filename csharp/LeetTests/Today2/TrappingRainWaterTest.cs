using Today2.TrappingRainWater;
namespace Today2;

internal class TrappingRainWaterTest
{
    [Test]
    public void Test1()
    {
        var solution = new Solution();
        var result = solution.Trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]);
        Assert.That(result, Is.EqualTo(6));
    }

    [Test]
    public void Test2()
    {
        var solution = new Solution();
        var result = solution.Trap([4, 2, 0, 3, 2, 5]);
        Assert.That(result, Is.EqualTo(9));
    }
}