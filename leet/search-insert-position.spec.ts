import { searchInsert, binarySearch } from './search-insert-position';

describe('Search Insert Position', () => {
  it('evaluates correctly', () => {
    expect(searchInsert([1, 3, 5, 6], 5)).toEqual(2);
    expect(searchInsert([1, 3, 5, 6], 2)).toEqual(1);
    expect(searchInsert([1, 3, 5, 6], 7)).toEqual(4);
  });

  it('evaluates binary search correctly', () => {
    expect(binarySearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], -99)).toEqual(-1);
    expect(binarySearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0)).toEqual(0);
    expect(binarySearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1)).toEqual(1);
    expect(binarySearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2)).toEqual(2);
    expect(binarySearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3)).toEqual(3);
    expect(binarySearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4)).toEqual(4);
    expect(binarySearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5)).toEqual(5);
    expect(binarySearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 6)).toEqual(6);
    expect(binarySearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 7)).toEqual(7);
    expect(binarySearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8)).toEqual(8);
    expect(binarySearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9)).toEqual(9);
    expect(binarySearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 34)).toEqual(-1);
  });
});
