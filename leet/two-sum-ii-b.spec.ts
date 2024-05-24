import { twoSum } from "./two-sum-ii-b";

describe("Two Sum II", () => {
  it("evaluates two sum correctly", () => {
    expect(twoSum([2, 7, 11, 15], 9)).toEqual([1, 2]);
    expect(twoSum([2, 3, 4], 6)).toEqual([1, 3]);
    expect(twoSum([-1, 0], -1)).toEqual([1, 2]);
    expect(twoSum([0, 0, 3, 4], 0)).toEqual([1, 2]);
    expect(twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8)).toEqual([4, 5]);
  });
});
