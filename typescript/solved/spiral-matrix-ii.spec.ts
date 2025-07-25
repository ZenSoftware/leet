import { generateMatrix } from './spiral-matrix-ii';

describe('Spiral Matrix II', () => {
  it('evaluates correctly 1', () => {
    expect(generateMatrix(3)).toEqual([
      [1, 2, 3],
      [8, 9, 4],
      [7, 6, 5],
    ]);
  });

  it('evaluates correctly 2', () => {
    expect(generateMatrix(1)).toEqual([[1]]);
  });

  it('evaluates correctly 3', () => {
    expect(generateMatrix(2)).toEqual([
      [1, 2],
      [4, 3],
    ]);
  });
});
