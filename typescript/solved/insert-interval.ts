/**
 * https://leetcode.com/problems/insert-interval/
 */

export function insert(intervals: number[][], newInterval: number[]): number[][] {
  intervals.push(newInterval);

  return merge(intervals);
}

function merge(intervals: number[][]): number[][] {
  intervals.sort((a, b) => {
    const first = a[0] - b[0];
    const second = a[1] - b[1];
    return first || second;
  });

  const result: number[][] = [];

  let accum = intervals[0];
  for (let i = 1; i < intervals.length; i++) {
    let combined = combineTwo(accum, intervals[i]);
    if (combined !== null) {
      accum = combined;
    } else {
      result.push(accum);
      accum = intervals[i];
    }
  }
  result.push(accum);

  return result;
}

function combineTwo(x: number[], y: number[]): number[] | null {
  if (y[0] <= x[1]) {
    const start = Math.min(x[0], y[0]);
    const end = Math.max(x[1], y[1]);
    return [start, end];
  }

  return null;
}
