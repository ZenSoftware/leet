import { MinStack } from './min-stack';

describe('Min Stack', () => {
  it('evaluates correctly', () => {
    const minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    expect(minStack.getMin()).toEqual(-3); // return -3
    minStack.pop();
    minStack.top(); // return 0
    expect(minStack.getMin()).toEqual(-2); // return -2
  });
});
