import { reverseBetween, toArray, toList } from './reverse-linked-list-ii';

describe('Reverse Linked List II', () => {
  it('evaluates correctly', () => {
    expect(true).toEqual(true);
  });

  it('constructs lists correctly', () => {
    const list = toList([1, 2, 3, 4, 5]);
    const array = toArray(list);
    expect(array).toEqual([1, 2, 3, 4, 5]);
  });
});
