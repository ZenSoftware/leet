// https://leetcode.com/problems/merge-intervals/description/
namespace Today2.MergeIntervals;

public class Solution
{
    public int[][] Merge(int[][] intervals)
    {
        Array.Sort(intervals, (a, b) => a[0].CompareTo(b[0]));
        var result = new List<int[]>();
        var i = 0;
        while (i < intervals.Length)
        {
            var largest = intervals[i][1];
            var j = i + 1;
            while (j < intervals.Length && largest >= intervals[j][0])
            {
                largest = Math.Max(largest, intervals[j][1]);
                j++;
            }
            result.Add([intervals[i][0], largest]);
            i = j;
        }
        return result.ToArray();
    }
}