import { rotateRight, rotateOnce, toArray, toList } from './rotate-list';

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

  it('evaluates rotateOnce correctly 1', () => {
    const input = toList([0, 1, 2]);
    const result = rotateOnce(input);
    expect(toArray(result)).toEqual([2, 0, 1]);
  });

  it('evaluates rotateOnce correctly 2', () => {
    const input = toList([0, 1]);
    const result = rotateOnce(input);
    expect(toArray(result)).toEqual([1, 0]);
  });

  it('evaluates rotateOnce correctly 3', () => {
    const input = toList([1]);
    const result = rotateOnce(input);
    expect(toArray(result)).toEqual([1]);
  });

  it('evaluates rotateOnce correctly 4', () => {
    const input = toList([]);
    const result = rotateOnce(input);
    expect(toArray(result)).toEqual([]);
  });

  it('constructs lists correctly', () => {
    const list = toList([1, 2, 3, 4]);
    const array = toArray(list);
    expect(array).toEqual([1, 2, 3, 4]);
  });
});
