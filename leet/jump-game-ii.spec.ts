import { jump } from './jump-game-ii';

describe('Jump Game II', () => {
  it('evaluates correctly', () => {
    expect(jump([2, 3, 1, 1, 4])).toEqual(2);
    expect(jump([2, 3, 0, 1, 4])).toEqual(2);
  });
});
