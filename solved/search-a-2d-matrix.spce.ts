import { searchMatrix } from './search-a-2d-matrix';

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
});
