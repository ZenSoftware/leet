using Today2.DailyTemperatures;
namespace Today2;

internal class DailyTemperaturesTest
{
    [Test]
    public void Test1()
    {
        var solution = new Solution();
        var result = solution.DailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]);
        Assert.That(result, Is.EqualTo([1, 1, 4, 2, 1, 1, 0, 0]));
    }

    [Test]
    public void Test2()
    {
        var solution = new Solution();
        var result = solution.DailyTemperatures([30, 40, 50, 60]);
        Assert.That(result, Is.EqualTo([1, 1, 1, 0]));
    }

    [Test]
    public void Test3()
    {
        var solution = new Solution();
        var result = solution.DailyTemperatures([30, 60, 90]);
        Assert.That(result, Is.EqualTo([1, 1, 0]));
    }
}