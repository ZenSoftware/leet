function insertionSort(nums: number[]): number[] {
  let i = 1;
  while (i < nums.length) {
    let j = i;
    while (nums[j - 1] >= nums[j]) {
      [nums[j], nums[j - 1]] = [nums[j - 1], nums[j]];
      j--;
    }
    i++;
  }
  return nums;
}

console.log(insertionSort([4, 6, 3, 9, 2, 7]));
