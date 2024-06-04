/**
 * https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
 */
export { evalRPN };

function evalRPN(tokens: string[]): number {
  const stack: number[] = [];

  for (let i = 0; i < tokens.length; i++) {
    if (tokens[i] === '+' || tokens[i] === '-' || tokens[i] === '*' || tokens[i] === '/') {
      const right = stack.pop() as number;
      const left = stack.pop() as number;
      let result: number;

      switch (tokens[i]) {
        case '+':
          result = left + right;
          break;
        case '-':
          result = left - right;
          break;
        case '*':
          result = left * right;
          break;
        case '/':
          const divided = left / right;
          if (divided < 0) result = Math.ceil(divided);
          else result = Math.floor(divided);
          break;
      }
      stack.push(result!);
    } else {
      const int = Number.parseInt(tokens[i]);
      stack.push(int);
    }
  }

  return stack[0];
}
