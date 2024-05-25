import { removeNthFromEnd, toList, toArray } from './remove-nth-node-from-end-of-list';

describe('Remove Nth Node From End of List', () => {
  it('evaluates correctly 1', () => {
    const list = toList([1, 2, 3, 4, 5]);
    const result = removeNthFromEnd(list, 2);
    expect(toArray(result)).toEqual([1, 2, 3, 5]);
  });

  it('evaluates correctly 2', () => {
    const list = toList([1]);
    const result = removeNthFromEnd(list, 1);
    expect(toArray(result)).toEqual([]);
  });

  it('evaluates correctly 3', () => {
    const list = toList([1, 2]);
    const result = removeNthFromEnd(list, 1);
    expect(toArray(result)).toEqual([1]);
  });
});
