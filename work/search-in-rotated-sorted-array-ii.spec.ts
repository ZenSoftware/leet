import { search, binarySearch } from './search-in-rotated-sorted-array-ii';

describe('Search in Rotated Sorted Array II', () => {
  it('evaluates correctly', () => {
    expect(search([2, 5, 6, 0, 0, 1, 2], 0)).toEqual(true);
    expect(search([2, 5, 6, 0, 0, 1, 2], 3)).toEqual(false);
  });

  it('evaluates binary search correctly', () => {
    const input1 = [0, 1, 2, 3, 4, 5];
    expect(binarySearch(input1, -1)).toEqual(-1);
    expect(binarySearch(input1, 0)).toEqual(0);
    expect(binarySearch(input1, 1)).toEqual(1);
    expect(binarySearch(input1, 2)).toEqual(2);
    expect(binarySearch(input1, 3)).toEqual(3);
    expect(binarySearch(input1, 4)).toEqual(4);
    expect(binarySearch(input1, 5)).toEqual(5);
    expect(binarySearch(input1, 6)).toEqual(-1);

    const input2 = [0, 1, 2, 3, 4, 5, 6];
    expect(binarySearch(input2, -1)).toEqual(-1);
    expect(binarySearch(input2, 0)).toEqual(0);
    expect(binarySearch(input2, 1)).toEqual(1);
    expect(binarySearch(input2, 2)).toEqual(2);
    expect(binarySearch(input2, 3)).toEqual(3);
    expect(binarySearch(input2, 4)).toEqual(4);
    expect(binarySearch(input2, 5)).toEqual(5);
    expect(binarySearch(input2, 6)).toEqual(6);
    expect(binarySearch(input2, 7)).toEqual(-1);
  });
});
