import { exist } from './word-search';

describe('Word Search', () => {
  it('evaluates correctly 1', () => {
    expect(
      exist(
        [
          ['A', 'B', 'C', 'E'],
          ['S', 'F', 'C', 'S'],
          ['A', 'D', 'E', 'E'],
        ],
        'ABCCED'
      )
    ).toEqual(true);
  });

  it('evaluates correctly 2', () => {
    expect(
      exist(
        [
          ['A', 'B', 'C', 'E'],
          ['S', 'F', 'C', 'S'],
          ['A', 'D', 'E', 'E'],
        ],
        'SEE'
      )
    ).toEqual(true);
  });

  it('evaluates correctly 3', () => {
    expect(
      exist(
        [
          ['A', 'B', 'C', 'E'],
          ['S', 'F', 'C', 'S'],
          ['A', 'D', 'E', 'E'],
        ],
        'ABCB'
      )
    ).toEqual(false);
  });

  it('evaluates correctly 4', () => {
    expect(exist([['a']], 'a')).toEqual(true);
  });

  it('evaluates correctly 5', () => {
    expect(
      exist(
        [
          ['a', 'b', 'c'],
          ['a', 'e', 'd'],
          ['a', 'f', 'g'],
        ],
        'abcdefg'
      )
    ).toEqual(true);
  });

  it('evaluates correctly 6', () => {
    expect(exist([['a', 'a']], 'aaa')).toEqual(false);
  });

  it('evaluates correctly 7', () => {
    expect(
      exist(
        [
          ['a', 'a'],
          ['A', 'A'],
        ],
        'aaa'
      )
    ).toEqual(false);
  });
});
