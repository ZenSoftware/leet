import { rotate } from './rotate-image';

describe('Rotate Image', () => {
  it('evaluates correctly', () => {
    const input = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
    ];
    rotate(input);
    expect(input).toEqual([
      [7, 4, 1],
      [8, 5, 2],
      [9, 6, 3],
    ]);
  });
});
