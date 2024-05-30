import { reverseBetween, toArray, toList } from './reverse-linked-list-ii';

describe('Reverse Linked List II', () => {
  it('evaluates correctly 1', () => {
    const input = toList([1, 2, 3, 4, 5]);
    expect(reverseBetween(input, 2, 4)).toEqual([1, 4, 3, 2, 5]);
  });

  it('evaluates correctly 2', () => {
    const input = toList([5]);
    expect(reverseBetween(input, 1, 1)).toEqual([5]);
  });

  it('constructs lists correctly', () => {
    const list = toList([1, 2, 3, 4, 5]);
    const array = toArray(list);
    expect(array).toEqual([1, 2, 3, 4, 5]);
  });
});
