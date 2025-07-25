import { searchInsert } from './search-insert-position';

describe('Search Insert Position', () => {
  it('evaluates search insert correctly', () => {
    expect(searchInsert([1, 3, 5, 6], 2)).toEqual(1);
    expect(searchInsert([1, 3, 5, 6], 7)).toEqual(4);
    expect(searchInsert([1, 3, 5, 6], 4)).toEqual(2);
  });
});
