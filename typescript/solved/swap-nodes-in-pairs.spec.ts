import { swapPairs, toArray, toList } from './swap-nodes-in-pairs';

describe('Swap Nodes in Pairs', () => {
  it('debugging', () => {
    const input = toList([1, 2, 3, 4, 5, 6, 7, 8, 9]);
    const result = swapPairs(input);
    expect(toArray(result)).toEqual([2, 1, 4, 3, 6, 5, 8, 7, 9]);
  });

  it('evaluates correctly 1', () => {
    const input = toList([1, 2, 3, 4]);
    const result = swapPairs(input);
    expect(toArray(result)).toEqual([2, 1, 4, 3]);
  });

  it('evaluates correctly 2', () => {
    const input = toList([]);
    const result = swapPairs(input);
    expect(toArray(result)).toEqual([]);
  });

  it('evaluates correctly 3', () => {
    const input = toList([1]);
    const result = swapPairs(input);
    expect(toArray(result)).toEqual([1]);
  });

  it('evaluates correctly 4', () => {
    const input = toList([1, 2, 3]);
    const result = swapPairs(input);
    expect(toArray(result)).toEqual([2, 1, 3]);
  });

  it('constructs lists correctly', () => {
    const list = toList([1, 2, 3, 4]);
    const array = toArray(list);
    expect(array).toEqual([1, 2, 3, 4]);
  });
});
