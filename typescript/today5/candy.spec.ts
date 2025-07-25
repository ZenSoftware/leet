import { candy } from './candy';

describe('Candy', () => {
  it('evaluates correctly', () => {
    expect(candy([1, 0, 2])).toEqual(5);
    expect(candy([1, 2, 2])).toEqual(4);
    expect(candy([1, 3, 4, 5, 2])).toEqual(11);
  });
});
