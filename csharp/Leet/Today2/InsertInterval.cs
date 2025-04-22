// https://leetcode.com/problems/insert-interval/description/
namespace Today2.InsertInterval;

public class Solution
{
    public int[][] Insert(int[][] intervals, int[] newInterval)
    {
        var insertionIndex = GetInsertionIndex(intervals, newInterval);
        intervals = [.. intervals[..insertionIndex], newInterval, .. intervals[insertionIndex..]];
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

    public int GetInsertionIndex(int[][] intervals, int[] newInterval)
    {
        int left = 0, right = intervals.Length - 1;
        while (left <= right)
        {
            var mid = left + ((right - left) / 2);
            if (newInterval[0] < intervals[mid][0])
                right = mid - 1;
            else if (intervals[mid][0] < newInterval[0])
                left = mid + 1;
            else
                return mid;
        }
        return left;
    }
}