/**
 * https://leetcode.com/problems/generate-parentheses/
 * only add parenthese if openCount < n
 * only add parenthese if closedCount < openCount
 * valid if open === closed === n
 */
export function generateParenthesis(n: number): string[] {
  const result: string[] = [];
  const stack: string[] = [];

  function gen(open: number, close: number) {
    if (open === n && close === n) {
      let concatenated = '';
      stack.forEach(s => (concatenated += s));
      result.push(concatenated);
      return;
    }

    if (open < n) {
      stack.push('(');
      gen(open + 1, close);
    }

    if (close < open) {
      stack.push(')');
      gen(open, close + 1);
    }
  }

  gen(0, 0);
  return result;
}
