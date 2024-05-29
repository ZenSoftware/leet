import { climbStairs } from './climbing-stairs';

describe('Climbing Stairs', () => {
  it('evaluates correctly', () => {
    expect(climbStairs(2)).toEqual(2);
    expect(climbStairs(3)).toEqual(3);
    expect(climbStairs(44)).toEqual(1134903170);
  });
});
