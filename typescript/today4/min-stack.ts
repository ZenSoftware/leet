/**
 * https://leetcode.com/problems/min-stack/
 */
export { MinStack };

class MinStack {
  stack: number[] = [];
  minimums: number[] = [];

  push(val: number): void {
    this.stack.push(val);

    if (this.minimums.length === 0) this.minimums.push(val);
    else {
      const currentMin = this.minimums[this.minimums.length - 1];
      this.minimums.push(Math.min(currentMin, val));
    }
  }

  pop(): void {
    this.stack.pop();
    this.minimums.pop();
  }

  top(): number {
    return this.stack[this.stack.length - 1];
  }

  getMin(): number {
    return this.minimums[this.stack.length - 1];
  }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
