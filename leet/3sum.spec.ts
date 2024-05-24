import { threeSum, binarySearch } from './3sum';

describe('3Sum', () => {
  it('evaluates 3Sum correctly', () => {
    expect(threeSum([-1, 0, 1, 2, -1, -4])).toEqual([
      [-1, -1, 2],
      [-1, 0, 1],
    ]);
    expect(threeSum([0, 1, 1])).toEqual([]);
    expect(threeSum([0, 0, 0])).toEqual([[0, 0, 0]]);
  });

  it('evaluates binary search correctly', () => {
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
