// https://leetcode.com/problems/non-overlapping-intervals/description/
namespace Today3.NonOverlappingIntervals;

public class Solution
{
    public int EraseOverlapIntervals(int[][] intervals)
    {
        Array.Sort(intervals, (a, b) => a[1].CompareTo(b[1]));
        var prev = intervals[0];
        var count = 1;
        for (int i = 1; i < intervals.Length; i++)
        {
            if (prev[1] <= intervals[i][0])
            {
                count++;
                prev = intervals[i];
            }
        }
        return intervals.Length - count;
    }
}