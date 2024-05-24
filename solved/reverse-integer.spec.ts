import { reverse } from './reverse-integer';

describe('Reverse Integer', () => {
  it('evaluates correctly', () => {
    expect(reverse(123)).toEqual(321);
    expect(reverse(-123)).toEqual(-321);
    expect(reverse(120)).toEqual(21);
  });
});
