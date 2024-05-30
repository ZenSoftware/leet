import { removeDuplicates } from './remove-duplicates-from-sorted-array-ii';

describe('Remove Duplicates from Sorted Array II', () => {
  it('evaluates correctly 1', () => {
    const input = [1, 1, 1, 2, 2, 3];
    expect(removeDuplicates(input)).toEqual(5);
    expect(input[0]).toEqual(1);
    expect(input[1]).toEqual(1);
    expect(input[2]).toEqual(2);
    expect(input[3]).toEqual(2);
    expect(input[4]).toEqual(3);
  });

  it('evaluates correctly 2', () => {
    const input = [0, 0, 1, 1, 1, 1, 2, 3, 3];
    expect(removeDuplicates(input)).toEqual(7);
    expect(input[0]).toEqual(0);
    expect(input[1]).toEqual(0);
    expect(input[2]).toEqual(1);
    expect(input[3]).toEqual(1);
    expect(input[4]).toEqual(2);
    expect(input[5]).toEqual(3);
    expect(input[6]).toEqual(3);
  });
});
