import { rotateRight, toArray, toList } from './rotate-list';

describe('Rotate List', () => {
  it('evaluates correctly 1', () => {
    const input = toList([1, 2, 3, 4, 5]);
    const result = rotateRight(input, 2);
    expect(toArray(result)).toEqual([4, 5, 1, 2, 3]);
  });

  it('evaluates correctly 2', () => {
    const input = toList([0, 1, 2]);
    const result = rotateRight(input, 4);
    expect(toArray(result)).toEqual([2, 0, 1]);
  });

  it('constructs lists correctly', () => {
    const list = toList([1, 2, 3, 4]);
    const array = toArray(list);
    expect(array).toEqual([1, 2, 3, 4]);
  });
});
