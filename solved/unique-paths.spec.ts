import { uniquePaths } from './unique-paths';

describe('Unique Paths', () => {
  it('evaluates correctly', () => {
    expect(uniquePaths(3, 7)).toEqual(28);
    expect(uniquePaths(3, 2)).toEqual(3);
  });
});
