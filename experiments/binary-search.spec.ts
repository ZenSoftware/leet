import { binarySearch } from "./binary-search";

describe("Binary Search", () => {
  it("evaluates correctly", () => {
    const sample = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    expect(binarySearch(sample, 1)).toEqual(0);
    expect(binarySearch(sample, 2)).toEqual(1);
    expect(binarySearch(sample, 3)).toEqual(2);
    expect(binarySearch(sample, 4)).toEqual(3);
    expect(binarySearch(sample, 5)).toEqual(4);
    expect(binarySearch(sample, 6)).toEqual(5);
    expect(binarySearch(sample, 7)).toEqual(6);
    expect(binarySearch(sample, 8)).toEqual(7);
    expect(binarySearch(sample, 9)).toEqual(8);
  });
});
