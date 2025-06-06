// https://leetcode.com/problems/rotting-oranges/description/
namespace Today4.RottingOranges;

public class Solution
{
    public int OrangesRotting(int[][] grid)
    {
        int ROWS = grid.Length;
        int COLS = grid[0].Length;

        bool BecameRotten((int Row, int Col) coord) =>
               (coord.Row - 1 >= 0 && grid[coord.Row - 1][coord.Col] == 2)
            || (coord.Row + 1 < ROWS && grid[coord.Row + 1][coord.Col] == 2)
            || (coord.Col - 1 >= 0 && grid[coord.Row][coord.Col - 1] == 2)
            || (coord.Col + 1 < COLS && grid[coord.Row][coord.Col + 1] == 2);

        var fresh = new HashSet<(int Row, int Col)>();
        for (int r = 0; r < ROWS; r++)
        {
            for (int c = 0; c < COLS; c++)
            {
                if (grid[r][c] == 1)
                    fresh.Add((r, c));
            }
        }

        int minutes = 0;
        var nextRotten = new HashSet<(int Row, int Col)>();
        while (fresh.Count > 0)
        {
            nextRotten.Clear();
            minutes++;

            foreach (var coord in fresh)
            {
                if (BecameRotten(coord))
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
        return minutes;
    }
}