import { twoSum, binarySearch } from "./two-sum-ii";

describe("Two Sum II", () => {
  it("evaluates correctly", () => {
    expect(twoSum([2, 7, 11, 15], 9)).toEqual([1, 2]);
    expect(twoSum([2, 3, 4], 6)).toEqual([1, 3]);
    expect(twoSum([-1, 0], -1)).toEqual([1, 2]);
  });

  it("evaluates binary search correctly", () => {
    const sample = [0, 2, 4, 6, 8, 10];
    expect(binarySearch(sample, 0)).toEqual(0);
    expect(binarySearch(sample, 2)).toEqual(1);
    expect(binarySearch(sample, 4)).toEqual(2);
    expect(binarySearch(sample, 6)).toEqual(3);
    expect(binarySearch(sample, 8)).toEqual(4);
    expect(binarySearch(sample, 10)).toEqual(5);
    expect(binarySearch(sample, -1)).toEqual(-1);
    expect(binarySearch(sample, 1)).toEqual(-1);
    expect(binarySearch(sample, 3)).toEqual(-1);
    expect(binarySearch(sample, 5)).toEqual(-1);
    expect(binarySearch(sample, 7)).toEqual(-1);
    expect(binarySearch(sample, 9)).toEqual(-1);
    expect(binarySearch(sample, 11)).toEqual(-1);
  });
});
