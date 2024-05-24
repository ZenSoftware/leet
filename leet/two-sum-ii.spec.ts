import { twoSum, binarySearch } from "./two-sum-ii";

describe("Two Sum II", () => {
  it("evaluates two sum correctly", () => {
    expect(twoSum([2, 7, 11, 15], 9)).toEqual([1, 2]);
    expect(twoSum([2, 3, 4], 6)).toEqual([1, 3]);
    expect(twoSum([-1, 0], -1)).toEqual([1, 2]);
    expect(twoSum([0, 0, 3, 4], 0)).toEqual([1, 2]);
    expect(twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8)).toEqual([4, 5]);
  });

  it("evaluates binary search correctly", () => {
    const sample = [0, 2, 4, 6, 8, 10];
    expect(binarySearch(sample, 0, -1)).toEqual(0);
    expect(binarySearch(sample, 2, -1)).toEqual(1);
    expect(binarySearch(sample, 4, -1)).toEqual(2);
    expect(binarySearch(sample, 6, -1)).toEqual(3);
    expect(binarySearch(sample, 8, -1)).toEqual(4);
    expect(binarySearch(sample, 10, -1)).toEqual(5);

    expect(binarySearch(sample, 0, 0)).toEqual(-1);
    expect(binarySearch(sample, 2, 1)).toEqual(-1);
    expect(binarySearch(sample, 4, 2)).toEqual(-1);
    expect(binarySearch(sample, 6, 3)).toEqual(-1);
    expect(binarySearch(sample, 8, 4)).toEqual(-1);
    expect(binarySearch(sample, 10, 5)).toEqual(-1);

    expect(binarySearch(sample, -1, -1)).toEqual(-1);
    expect(binarySearch(sample, 1, -1)).toEqual(-1);
    expect(binarySearch(sample, 3, -1)).toEqual(-1);
    expect(binarySearch(sample, 5, -1)).toEqual(-1);
    expect(binarySearch(sample, 7, -1)).toEqual(-1);
    expect(binarySearch(sample, 9, -1)).toEqual(-1);
    expect(binarySearch(sample, 11, -1)).toEqual(-1);
  });
});
