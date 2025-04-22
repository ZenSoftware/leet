using Today2.BasicCalculator;
namespace Today2;

internal class BasicCalculatorTest
{
    [Test]
    public void Test1()
    {
        var solution = new Solution();
        var result = solution.Calculate("1 + 1");
        Assert.That(result, Is.EqualTo(2));
    }

    [Test]
    public void Test2()
    {
        var solution = new Solution();
        var result = solution.Calculate(" 2-1 + 2 ");
        Assert.That(result, Is.EqualTo(3));
    }

    [Test]
    public void Test3()
    {
        var solution = new Solution();
        var result = solution.Calculate("(1+(4+5+2)-3)+(6+8)");
        Assert.That(result, Is.EqualTo(23));
    }
}