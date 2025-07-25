/**
 * https://leetcode.com/problems/merge-sorted-array/description/
 */
export { merge };

function merge(nums1: number[], m: number, nums2: number[], n: number): void {
  const solution: number[] = Array(m + n);

  let iS = 0;
  let i1 = 0;
  let i2 = 0;
  while (i1 < m && i2 < n) {
    if (nums1[i1] < nums2[i2]) {
      solution[iS] = nums1[i1];
      i1++;
    } else {
      solution[iS] = nums2[i2];
      i2++;
    }
    iS++;
  }

  while (i1 < m) {
    solution[iS] = nums1[i1];
    iS++;
    i1++;
  }

  while (i2 < n) {
    solution[iS] = nums2[i2];
    iS++;
    i2++;
  }

  for (let i = 0; i < m + n; i++) {
    nums1[i] = solution[i];
  }
}
