// https://leetcode.com/problems/largest-rectangle-in-histogram/description/
namespace Today2.LargestRectangleInHistogram;

public class Solution
{
    public int LargestRectangleArea(int[] heights)
    {
        var result = 0;
        var stack = new Stack<(int Index, int Height)>();
        stack.Push((-1, 0));
        for (int i = 0; i < heights.Length; i++)
        {
            var lastIndex = i;
            while (heights[i] < stack.Peek().Height)
            {
                var (index, height) = stack.Pop();
                var area = (i - index) * height;
                result = Math.Max(result, area);
                lastIndex = index;
            }
            stack.Push((lastIndex, heights[i]));
        }

        while (stack.Count > 0)
        {
            var (index, height) = stack.Pop();
            var area = (heights.Length - index) * height;
            result = Math.Max(result, area);
        }

        return result;
    }
}