using Leet.ValidParentheses;

namespace LeetTests.Today1;

internal class ValidParenthesesTest
{
    [Test]
    public void TestValidParentheses()
    {
        var solution = new Solution();
        Assert.That(solution.IsValid("()"), Is.EqualTo(true));
        Assert.That(solution.IsValid("()[]{}"), Is.EqualTo(true));
        Assert.That(solution.IsValid("(]"), Is.EqualTo(false));
        Assert.That(solution.IsValid("([])"), Is.EqualTo(true));
    }
}