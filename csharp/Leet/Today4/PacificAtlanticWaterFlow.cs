// https://leetcode.com/problems/pacific-atlantic-water-flow/description/
namespace Today4.PacificAtlanticWaterFlow;

public class Solution
{
    public IList<IList<int>> PacificAtlantic(int[][] heights)
    {
        var ROWS = heights.Length;
        var COLS = heights[0].Length;
        var result = new List<IList<int>>();
        var visited = new HashSet<(int, int)>();

        bool IsPacificFlow(int row, int col, int prev)
        {
            if (row < 0 || col < 0)
                return true;
            if (row >= ROWS || col >= COLS || heights[row][col] > prev || visited.Contains((row, col)))
                return false;

            visited.Add((row, col));
            var result = false;
            var cur = heights[row][col];
            if (IsPacificFlow(row - 1, col, cur)
                || IsPacificFlow(row + 1, col, cur)
                || IsPacificFlow(row, col - 1, cur)
                || IsPacificFlow(row, col + 1, cur))
            {
                result = true;
            }
            visited.Remove((row, col));
            return result;
        }

        bool IsAtlanticFlow(int row, int col, int prev)
        {
            if (row >= ROWS || col >= COLS)
                return true;
            if (row < 0 || col < 0 || heights[row][col] > prev || visited.Contains((row, col)))
                return false;

            visited.Add((row, col));
            var result = false;
            var cur = heights[row][col];
            if (IsAtlanticFlow(row - 1, col, cur)
                || IsAtlanticFlow(row + 1, col, cur)
                || IsAtlanticFlow(row, col - 1, cur)
                || IsAtlanticFlow(row, col + 1, cur))
            {
                result = true;
            }
            visited.Remove((row, col));
            return result;
        }

        for (int i = 0; i < ROWS; i++)
        {
            for (int j = 0; j < COLS; j++)
            {
                if (IsPacificFlow(i, j, int.MaxValue) && IsAtlanticFlow(i, j, int.MaxValue))
                    result.Add([i, j]);
            }
        }

        return result;
    }
}