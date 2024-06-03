import { binarySearch } from './binary-search2';

describe('Binary Search', () => {
  it('evaluates correectly', () => {
    const input = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    expect(binarySearch(input, -1)).toEqual(-1);
    expect(binarySearch(input, 0)).toEqual(0);
    expect(binarySearch(input, 1)).toEqual(1);
    expect(binarySearch(input, 2)).toEqual(2);
    expect(binarySearch(input, 3)).toEqual(3);
    expect(binarySearch(input, 4)).toEqual(4);
    expect(binarySearch(input, 5)).toEqual(5);
    expect(binarySearch(input, 6)).toEqual(6);
    expect(binarySearch(input, 7)).toEqual(7);
    expect(binarySearch(input, 8)).toEqual(8);
    expect(binarySearch(input, 9)).toEqual(9);
    expect(binarySearch(input, 10)).toEqual(-1);
  });
});
