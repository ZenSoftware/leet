/**
 * https://leetcode.com/problems/valid-parentheses/description/
 */
export function isValid(s: string): boolean {
  const history: string[] = [];
  const openBrackets = ['(', '[', '{'];

  for (let char of s) {
    if (openBrackets.includes(char)) {
      history.push(char);
    } else {
      const last = history.pop();
      if (last === '(' && char === ')') continue;
      else if (last === '[' && char === ']') continue;
      else if (last === '{' && char === '}') continue;
      return false;
    }
  }

  return history.length === 0;
}
