import { searchMatrix, binarySearchRow, binarySearchCol } from './search-a-2d-matrix';

describe('Search a 2D Matrix', () => {
  it('evaluates correctly 1', () => {
    const input = [
      [1, 3, 5, 7],
      [10, 11, 16, 20],
      [23, 30, 34, 60],
    ];
    expect(searchMatrix(input, 3)).toEqual(true);
  });

  it('evaluates correctly 2', () => {
    const input = [
      [1, 3, 5, 7],
      [10, 11, 16, 20],
      [23, 30, 34, 60],
    ];
    expect(searchMatrix(input, 13)).toEqual(false);
  });

  it('evaluates correctly 3', () => {
    const input = [
      [1, 3, 5, 7],
      [10, 11, 16, 20],
      [23, 30, 34, 50],
    ];
    expect(searchMatrix(input, 11)).toEqual(true);
  });

  it('evaluates binary search row correctly', () => {
    const input = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    expect(binarySearchRow(input, -1)).toEqual(false);
    expect(binarySearchRow(input, 0)).toEqual(true);
    expect(binarySearchRow(input, 1)).toEqual(true);
    expect(binarySearchRow(input, 2)).toEqual(true);
    expect(binarySearchRow(input, 3)).toEqual(true);
    expect(binarySearchRow(input, 4)).toEqual(true);
    expect(binarySearchRow(input, 5)).toEqual(true);
    expect(binarySearchRow(input, 6)).toEqual(true);
    expect(binarySearchRow(input, 7)).toEqual(true);
    expect(binarySearchRow(input, 8)).toEqual(true);
    expect(binarySearchRow(input, 9)).toEqual(true);
    expect(binarySearchRow(input, 10)).toEqual(false);
  });

  it('evaluates search first column correctly', () => {
    const input = [
      [1, 3, 5, 7],
      [10, 11, 16, 20],
      [23, 30, 34, 60],
    ];

    expect(binarySearchCol(input, 5)).toEqual(0);
    expect(binarySearchCol(input, 11)).toEqual(1);
    expect(binarySearchCol(input, 30)).toEqual(2);
  });
});
