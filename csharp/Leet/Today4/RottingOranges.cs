// https://leetcode.com/problems/rotting-oranges/description/
namespace Today4.RottingOranges;

public class Solution
{
    public int OrangesRotting(int[][] grid)
    {
        int ROWS = grid.Length;
        int COLS = grid[0].Length;

        var fresh = new HashSet<(int Row, int Col)>();
        for (int r = 0; r < ROWS; r++)
        {
            for (int c = 0; c < COLS; c++)
            {
                if (grid[r][c] == 1)
                    fresh.Add((r, c));
            }
        }

        int count = 0;
        var nextRotten = new HashSet<(int Row, int Col)>();
        while (fresh.Count > 0)
        {
            nextRotten.Clear();
            count++;

            foreach (var coord in fresh)
            {
                if (BecameRotten(grid, coord))
                    nextRotten.Add(coord);
            }

            if (nextRotten.Count == 0)
                return -1;


            foreach (var coord in nextRotten)
            {
                grid[coord.Row][coord.Col] = 2;
                fresh.Remove(coord);
            }
        }
        return count;
    }

    private bool BecameRotten(int[][] grid, (int Row, int Col) coord)
    {
        if (coord.Row - 1 >= 0 && grid[coord.Row - 1][coord.Col] == 2)
            return true;
        if (coord.Row + 1 < grid.Length && grid[coord.Row + 1][coord.Col] == 2)
            return true;
        if (coord.Col - 1 >= 0 && grid[coord.Row][coord.Col - 1] == 2)
            return true;
        if (coord.Col + 1 < grid[0].Length && grid[coord.Row][coord.Col + 1] == 2)
            return true;
        return false;
    }
}