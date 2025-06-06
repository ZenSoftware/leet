// https://leetcode.com/problems/insert-interval/description/
namespace Today2.InsertInterval;

public class Solution
{
    public int[][] Insert(int[][] intervals, int[] newInterval)
    {
        var result = new List<int[]>();
        var i = 0;
        while (i < intervals.Length && intervals[i][1] < newInterval[0])
        {
            result.Add(intervals[i]);
            i++;
        }

        while (i < intervals.Length && newInterval[1] >= intervals[i][0])
        {
            newInterval[0] = Math.Min(newInterval[0], intervals[i][0]);
            newInterval[1] = Math.Max(newInterval[1], intervals[i][1]);
            i++;
        }
        result.Add(newInterval);

        while (i < intervals.Length)
        {
            result.Add(intervals[i]);
            i++;
        }

        return result.ToArray();
    }
}