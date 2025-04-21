using Leet.EvaluateReversePolishNotation;

namespace LeetTests;

internal class EvaluateReversePolishNotationTest
{
    [Test]
    public void TestEvaluateReversePolishNotation()
    {
        var solution = new Solution();
        var result = solution.EvalRPN(["2", "1", "+", "3", "*"]);
        Assert.That(result, Is.EqualTo(9));
    }

    [Test]
    public void TestEvaluateReversePolishNotation2()
    {
        var solution = new Solution();
        var result = solution.EvalRPN(["4", "13", "5", "/", "+"]);
        Assert.That(result, Is.EqualTo(6));
    }

}