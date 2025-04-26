using Today4.MergeKSortedLists;
namespace Today4;

internal class MergeKSortedListsTest
{
    [Test]
    public void Test1()
    {
        var solution = new Solution();
        var lists = ToLists([[1, 4, 5], [1, 3, 4], [2, 6]]);
        var result = solution.MergeKLists(lists);
        int[] answer = [1, 1, 2, 3, 4, 4, 5, 6];
        Assert.That(LeetList.ToArray(result), Is.EqualTo(answer));
    }

    [Test]
    public void Test2()
    {
        var solution = new Solution();
        var lists = ToLists([]);
        var result = solution.MergeKLists(lists);
        int[] answer = [];
        Assert.That(LeetList.ToArray(result), Is.EqualTo(answer));
    }

    [Test]
    public void Test3()
    {
        var solution = new Solution();
        var lists = ToLists([[]]);
        var result = solution.MergeKLists(lists);
        int[] answer = [];
        Assert.That(LeetList.ToArray(result), Is.EqualTo(answer));
    }

    private ListNode[] ToLists(int[][] lists)
    {
        var result = new List<ListNode>();
        foreach (var list in lists)
        {
            result.Add(LeetList.ToList(list));
        }
        return result.ToArray();
    }
}