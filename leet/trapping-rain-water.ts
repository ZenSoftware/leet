/**
 * https://leetcode.com/problems/trapping-rain-water/description/
 */
export function trap(height: number[]): number {
  let result = 0;
  let maxL: Max = { index: -1, height: 0 };
  let maxR: Max = { index: -1, height: 0 };

  for (let i = 1; i < height.length; i++) {
    if (height[i] > maxR.height) {
      maxR.index = i;
      maxR.height = height[i];
    }
  }

  for (let i = 0; i < height.length; i++) {
    setMaxL(height, i, maxL);
    setMaxR(height, i, maxR);
    const max = Math.min(maxL.height, maxR.height);
    let volume = max - height[i];
    if (volume < 0) volume = 0;
    result += volume;
  }

  return result;
}

function setMaxL(height: number[], from: number, max: Max) {
  if (from <= 0) return;

  if (height[from - 1] > max.height) {
    max.index = from - 1;
    max.height = height[from - 1];
  }
}

function setMaxR(height: number[], from: number, max: Max) {
  if (from >= height.length - 1) {
    max.index = height.length;
    max.height = 0;
    return;
  }

  if (from >= max.index) {
    max.height = 0;
    for (let i = from + 1; i < height.length; i++) {
      if (height[i] > max.height) {
        max.index = i;
        max.height = height[i];
      }
    }
  }
}

interface Max {
  index: number;
  height: number;
}
