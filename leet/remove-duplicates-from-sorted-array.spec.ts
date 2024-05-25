import { removeDuplicates } from './remove-duplicates-from-sorted-array';

describe('Remove Duplicates from Sorted Array', () => {
  it('evaluates correctly 1', () => {
    const input = [1, 1, 2];
    expect(removeDuplicates(input)).toEqual(2);
    expect(input[0]).toEqual(1);
    expect(input[1]).toEqual(2);
  });

  it('evaluates correctly 2', () => {
    const input: number[] = [];
    expect(removeDuplicates(input)).toEqual(0);
  });

  it('evaluates correctly 3', () => {
    const input = [1];
    expect(removeDuplicates(input)).toEqual(1);
    expect(input[0]).toEqual(1);
  });

  it('evaluates correctly 4', () => {
    const input = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4];
    expect(removeDuplicates(input)).toEqual(5);
    expect(input[0]).toEqual(0);
    expect(input[1]).toEqual(1);
    expect(input[2]).toEqual(2);
    expect(input[3]).toEqual(3);
    expect(input[4]).toEqual(4);
  });
});
