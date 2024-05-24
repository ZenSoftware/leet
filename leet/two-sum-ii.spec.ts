import { twoSum, binarySearch } from "./two-sum-ii";

describe("", () => {
  it("evaluates correctly", () => {
    expect(twoSum([2, 7, 11, 15], 9)).toEqual([1, 2]);
    expect(twoSum([2, 3, 4], 6)).toEqual([1, 3]);
    expect(twoSum([-1, 0], -1)).toEqual([1, 2]);
  });

  it("evaluates binary search correctly", () => {
    expect(binarySearch([2, 7, 11, 15], 7)).toEqual(1);
  });
});