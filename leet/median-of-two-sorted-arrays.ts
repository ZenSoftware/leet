/**
 * https://leetcode.com/problems/median-of-two-sorted-arrays/description/
 */
export function findMedianSortedArrays(
  nums1: number[],
  nums2: number[]
): number {
  const merged: number[] = Array(nums1.length + nums2.length);
  let mergedIndex = 0;
  let i = 0;
  let j = 0;

  while (i < nums1.length || j < nums2.length) {
    if (i >= nums1.length) {
      merged[mergedIndex] = nums2[j];
      mergedIndex++;
      j++;
      continue;
    } else if (j >= nums2.length) {
      merged[mergedIndex] = nums1[i];
      mergedIndex++;
      i++;
      continue;
    }

    if (nums1[i] < nums2[j]) {
      merged[mergedIndex] = nums1[i];
      mergedIndex++;
      i++;
    } else {
      merged[mergedIndex] = nums2[j];
      mergedIndex++;
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
