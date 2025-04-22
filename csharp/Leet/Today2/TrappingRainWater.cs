namespace Today2.TrappingRainWater;

/// <summary>
/// Time: O(n)
/// Space: O(n)
/// </summary>
public class Solution
{
    public int Trap(int[] height)
    {
        var max = 0;
        var maxLeft = new int[height.Length];
        for (int i = 0; i < height.Length; i++)
        {
            maxLeft[i] = max;
            max = Math.Max(max, height[i]);
        }

        max = 0;
        var maxRight = new int[height.Length];
        for (int i = height.Length - 1; i >= 0; i--)
        {
            maxRight[i] = max;
            max = Math.Max(max, height[i]);
        }

        var result = 0;
        for (int i = 0; i < height.Length; i++)
        {
            var min = Math.Min(maxLeft[i], maxRight[i]);
            var vol = min - height[i];
            result += Math.Max(vol, 0);
        }
        return result;
    }
}