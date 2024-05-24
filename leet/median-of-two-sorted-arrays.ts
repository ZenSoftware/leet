/**
 * https://leetcode.com/problems/median-of-two-sorted-arrays/description/
 */
export function findMedianSortedArrays(
  nums1: number[],
  nums2: number[]
): number {
  const merged: number[] = [];
  let i = 0;
  let j = 0;

  while (i < nums1.length || j < nums2.length) {
    if (i >= nums1.length) {
      merged.push(nums2[j]);
      j++;
      continue;
    } else if (j >= nums2.length) {
      merged.push(nums1[i]);
      i++;
      continue;
    }

    if (nums1[i] < nums2[j]) {
      merged.push(nums1[i]);
      i++;
    } else {
      merged.push(nums2[j]);
      j++;
    }
  }

  if (merged.length % 2 === 1) {
    const index = Math.floor(merged.length / 2);
    return merged[index];
  } else {
    const half = merged.length / 2;
    return (merged[half] + merged[half - 1]) / 2;
  }
}
