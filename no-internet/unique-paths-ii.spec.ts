import { uniquePathsWithObstacles } from './unique-paths-ii';

describe('Unique Paths II', () => {
  it('evaluates correctly 1', () => {
    const input = [
      [0, 0, 0],
      [0, 1, 0],
      [0, 0, 0],
    ];
    expect(uniquePathsWithObstacles(input)).toEqual(2);
  });

  it('evaluates correctly 2', () => {
    const input = [
      [0, 1],
      [0, 0],
    ];
    expect(uniquePathsWithObstacles(input)).toEqual(1);
  });
});
