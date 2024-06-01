/**
 * https://leetcode.com/problems/valid-palindrome/description/
 */
export { isPalindrome, cleanString };

function isPalindrome(s: string): boolean {
  const cleaned = cleanString(s);
  let left = 0;
  let right = cleaned.length - 1;

  while (left < right) {
    if (cleaned[left] !== cleaned[right]) return false;
    left++;
    right--;
  }

  return true;
}

function cleanString(s: string): string {
  s = s.toLowerCase();
  let result = '';
  for (let i = 0; i < s.length; i++) {
    const charCode = s.charCodeAt(i);
    if ((97 <= charCode && charCode <= 122) || (48 <= charCode && charCode <= 57)) {
      result += s[i];
    }
  }
  return result;
}
