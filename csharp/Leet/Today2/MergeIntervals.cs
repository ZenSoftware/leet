namespace Today2.MergeIntervals;

public class Solution
{
    public int[][] Merge(int[][] intervals)
    {
        Array.Sort(intervals, (x, y) => x[0].CompareTo(y[0]));
        var i = 0;
        var result = new List<int[]>();
        while (i < intervals.Length)
        {
            var j = i;
            var largest = intervals[i][1];
            while (j + 1 < intervals.Length && largest >= intervals[j + 1][0])
            {
                j++;
                largest = Math.Max(largest, intervals[j][1]);
            }
            result.Add([intervals[i][0], largest]);
            i = j + 1;
        }
        return result.ToArray();
    }
}