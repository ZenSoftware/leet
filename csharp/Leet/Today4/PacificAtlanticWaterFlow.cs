// https://leetcode.com/problems/pacific-atlantic-water-flow/description/
namespace Today4.PacificAtlanticWaterFlow;

public class Solution
{
    public IList<IList<int>> PacificAtlantic(int[][] heights)
    {
        var ROWS = heights.Length;
        var COLS = heights[0].Length;
        var result = new List<IList<int>>();
        var visited = new bool[ROWS][];
        for (int row = 0; row < ROWS; row++)
        {
            visited[row] = new bool[COLS];
        }

        bool IsPacificFlow(int row, int col, int prev)
        {
            if (row < 0 || col < 0)
                return true;
            if (row >= ROWS || col >= COLS || heights[row][col] > prev || visited[row][col])
                return false;

            visited[row][col] = true;
            var cur = heights[row][col];
            var result = IsPacificFlow(row - 1, col, cur)
                || IsPacificFlow(row, col - 1, cur)
                || IsPacificFlow(row + 1, col, cur)
                || IsPacificFlow(row, col + 1, cur);
            visited[row][col] = false;
            return result;
        }

        bool IsAtlanticFlow(int row, int col, int prev)
        {
            if (row >= ROWS || col >= COLS)
                return true;
            if (row < 0 || col < 0 || heights[row][col] > prev || visited[row][col])
                return false;

            visited[row][col] = true;
            var cur = heights[row][col];
            var result = IsAtlanticFlow(row + 1, col, cur)
                || IsAtlanticFlow(row, col + 1, cur)
                || IsAtlanticFlow(row - 1, col, cur)
                || IsAtlanticFlow(row, col - 1, cur);
            visited[row][col] = false;
            return result;
        }

        for (int row = 0; row < ROWS; row++)
        {
            for (int col = 0; col < COLS; col++)
            {
                if (IsPacificFlow(row, col, int.MaxValue) && IsAtlanticFlow(row, col, int.MaxValue))
                    result.Add([row, col]);
            }
        }

        return result;
    }
}