// https://leetcode.com/problems/trapping-rain-water/description/
namespace Today2.TrappingRainWater;

/// <summary>
/// Time: O(n)
/// Space: O(1)
/// </summary>
public class Solution
{
    public int Trap(int[] height)
    {
        int l = 0, r = height.Length - 1;
        int maxL = height[l], maxR = height[r];
        int result = 0;

        while (l < r)
        {
            if (maxL <= maxR)
            {
                l++;
                maxL = Math.Max(maxL, height[l]);
                result += maxL - height[l];
            }
            else
            {
                r--;
                maxR = Math.Max(maxR, height[r]);
                result += maxR - height[r];
            }
        }

        return result;
    }
}