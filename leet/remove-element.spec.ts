import { removeElement } from './remove-element';

describe('Remove Element', () => {
  it('evaluates correctly 1', () => {
    const input = [3, 2, 2, 3];
    expect(removeElement(input, 3)).toEqual(2);
    expect(input[0]).toEqual(2);
    expect(input[1]).toEqual(2);
  });

  it('evaluates correctly 2', () => {
    const input = [0, 1, 2, 2, 3, 0, 4, 2];
    expect(removeElement(input, 2)).toEqual(5);
    expect(input[0]).toEqual(0);
    expect(input[1]).toEqual(1);
    expect(input[2]).toEqual(3);
    expect(input[3]).toEqual(0);
    expect(input[4]).toEqual(4);
  });
});
