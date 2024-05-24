import { twoSum, binarySearch } from "./two-sum-ii";

describe("Two Sum II", () => {
  it("evaluates correctly", () => {
    expect(twoSum([2, 7, 11, 15], 9)).toEqual([1, 2]);
    expect(twoSum([2, 3, 4], 6)).toEqual([1, 3]);
    expect(twoSum([-1, 0], -1)).toEqual([1, 2]);
  });

  it("evaluates binary search correctly", () => {
    expect(binarySearch([0, 2, 4, 6, 8, 10], 0)).toEqual(0);
    expect(binarySearch([0, 2, 4, 6, 8, 10], 2)).toEqual(1);
    expect(binarySearch([0, 2, 4, 6, 8, 10], 4)).toEqual(2);
    expect(binarySearch([0, 2, 4, 6, 8, 10], 6)).toEqual(3);
    expect(binarySearch([0, 2, 4, 6, 8, 10], 8)).toEqual(4);
    expect(binarySearch([0, 2, 4, 6, 8, 10], 10)).toEqual(5);
    expect(binarySearch([0, 2, 4, 6, 8, 10], -1)).toEqual(-1);
    expect(binarySearch([0, 2, 4, 6, 8, 10], 1)).toEqual(-1);
    expect(binarySearch([0, 2, 4, 6, 8, 10], 3)).toEqual(-1);
    expect(binarySearch([0, 2, 4, 6, 8, 10], 5)).toEqual(-1);
    expect(binarySearch([0, 2, 4, 6, 8, 10], 7)).toEqual(-1);
    expect(binarySearch([0, 2, 4, 6, 8, 10], 9)).toEqual(-1);
    expect(binarySearch([0, 2, 4, 6, 8, 10], 11)).toEqual(-1);
  });
});
