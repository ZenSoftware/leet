import { searchMatrix, binarySearch } from './search-a-2d-matrix';

describe('Search a 2D Matrix', () => {
  it('evaluates correctly 1', () => {
    const input = [
      [1, 3, 5, 7],
      [10, 11, 16, 20],
      [23, 30, 34, 60],
    ];
    expect(searchMatrix(input, 3)).toEqual(true);
  });

  it('evaluates correctly 1', () => {
    const input = [
      [1, 3, 5, 7],
      [10, 11, 16, 20],
      [23, 30, 34, 60],
    ];
    expect(searchMatrix(input, 13)).toEqual(false);
  });

  it('evaluates binary search correctly', () => {
    const input = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    expect(binarySearch(input, -1)).toEqual(false);
    expect(binarySearch(input, 0)).toEqual(true);
    expect(binarySearch(input, 1)).toEqual(true);
    expect(binarySearch(input, 2)).toEqual(true);
    expect(binarySearch(input, 3)).toEqual(true);
    expect(binarySearch(input, 4)).toEqual(true);
    expect(binarySearch(input, 5)).toEqual(true);
    expect(binarySearch(input, 6)).toEqual(true);
    expect(binarySearch(input, 7)).toEqual(true);
    expect(binarySearch(input, 8)).toEqual(true);
    expect(binarySearch(input, 9)).toEqual(true);
    expect(binarySearch(input, 10)).toEqual(false);
  });
});
