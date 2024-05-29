import {
  searchRange,
  binarySearch,
} from './find-first-and-last-position-of-element-in-sorted-array';

describe('Find First and Last Position of Element in Sorted Array', () => {
  it('evaluates correctly', () => {
    expect(searchRange([5, 7, 7, 8, 8, 10], 8)).toEqual([3, 4]);
    expect(searchRange([5, 7, 7, 8, 8, 10], 6)).toEqual([-1, -1]);
    expect(searchRange([], 0)).toEqual([-1, -1]);
  });

  it('evaluates binary search correctly', () => {
    expect(binarySearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], -1)).toEqual(-1);
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
    expect(binarySearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)).toEqual(-1);
  });
});
