/**
 * https://leetcode.com/problems/palindrome-partitioning/description/
 */
export { partition };

function partition(s: string): string[][] {
  const result: string[][] = [];

  function backtrack(start: number, path: string[]) {
    if (start >= s.length) {
      result.push([...path]);
      return;
    }

    for (let end = start + 1; end <= s.length; end++) {
      const evaluate = s.substring(start, end);
      if (isPalindrome(evaluate)) {
        path.push(evaluate);
        backtrack(end, path);
        path.pop();
      }
    }
  }

  backtrack(0, []);
  return result;
}

function isPalindrome(s: string): boolean {
  let l = 0;
  let r = s.length - 1;
  while (l < r) {
    if (s[l] !== s[r]) return false;
    l++;
    r--;
  }
  return true;
}
