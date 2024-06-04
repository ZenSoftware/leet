import { search } from './search-in-rotated-sorted-array';

describe('Search in Rotated Sorted Array', () => {
  it('evaluates correctly', () => {
    expect(search([4, 5, 6, 7, 0, 1, 2], 4)).toEqual(0);
    expect(search([4, 5, 6, 7, 0, 1, 2], 5)).toEqual(1);
    expect(search([4, 5, 6, 7, 0, 1, 2], 6)).toEqual(2);
    expect(search([4, 5, 6, 7, 0, 1, 2], 7)).toEqual(3);
    expect(search([4, 5, 6, 7, 0, 1, 2], 0)).toEqual(4);
    expect(search([4, 5, 6, 7, 0, 1, 2], 1)).toEqual(5);
    expect(search([4, 5, 6, 7, 0, 1, 2], 2)).toEqual(6);
    expect(search([4, 5, 6, 7, 0, 1, 2], 3)).toEqual(-1);
    expect(search([4, 5, 6, 7, 0, 1, 2], 8)).toEqual(-1);
    expect(search([1], 0)).toEqual(-1);
    expect(search([3, 1], 1)).toEqual(1);
  });
});
