using Today4.CourseSchedule;
namespace Today4;

internal class CourseScheduleTest
{
    [Test]
    public void Test1()
    {
        var solution = new Solution();
        var result = solution.CanFinish(2, [[1, 0]]);
        Assert.That(result, Is.EqualTo(true));
    }

    [Test]
    public void Test2()
    {
        var solution = new Solution();
        var result = solution.CanFinish(2, [[1, 0], [0, 1]]);
        Assert.That(result, Is.EqualTo(false));
    }
}