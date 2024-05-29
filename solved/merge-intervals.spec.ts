import { merge, combineTwo } from './merge-intervals';

describe('Merge Intervals', () => {
  it('evaluates correctly 1', () => {
    expect(
      merge([
        [1, 3],
        [2, 6],
        [8, 10],
        [15, 18],
      ])
    ).toEqual([
      [1, 6],
      [8, 10],
      [15, 18],
    ]);
  });

  it('evaluates correctly 2', () => {
    expect(
      merge([
        [1, 4],
        [4, 5],
      ])
    ).toEqual([[1, 5]]);
  });

  it('evaluates correctly 3', () => {
    expect(
      merge([
        [1, 4],
        [2, 3],
      ])
    ).toEqual([[1, 4]]);
  });

  it('evaluates combine two correctly', () => {
    expect(combineTwo([1, 4], [3, 5])).toEqual([1, 5]);
    expect(combineTwo([1, 4], [4, 5])).toEqual([1, 5]);
    expect(combineTwo([1, 2], [4, 5])).toEqual(null);
    expect(combineTwo([1, 4], [2, 3])).toEqual([1, 4]);
  });
});
