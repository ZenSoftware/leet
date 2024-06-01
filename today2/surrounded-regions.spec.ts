import { solve } from './surrounded-regions';

describe('Surrounded Regions', () => {
  it('evaluates correctly 1', () => {
    const input = [['X']];
    solve(input);
    expect(input).toEqual([['X']]);
  });

  it('evaluates correctly 2', () => {
    const input = [
      ['X', 'X', 'X', 'X'],
      ['X', 'O', 'O', 'X'],
      ['X', 'X', 'O', 'X'],
      ['X', 'O', 'X', 'X'],
    ];
    solve(input);
    expect(input).toEqual([
      ['X', 'X', 'X', 'X'],
      ['X', 'O', 'O', 'X'],
      ['X', 'X', 'O', 'X'],
      ['X', 'O', 'X', 'X'],
    ]);
  });
});
