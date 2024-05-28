import { rotateRight, toArray, toList } from './rotate-list';

describe('Rotate List', () => {
  it('evaluates correctly', () => {
    expect(false).toEqual(true);
  });

  it('constructs lists correctly', () => {
    const list = toList([1, 2, 3, 4]);
    const array = toArray(list);
    expect(array).toEqual([1, 2, 3, 4]);
  });
});
