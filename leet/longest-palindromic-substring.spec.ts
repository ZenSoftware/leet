import {
  longestPalindrome,
  isPalindrome,
} from "./longest-palindromic-substring";

describe("Longest Palindromic Substring", () => {
  it("evaluates longestPalindrome correctly", () => {
    expect(longestPalindrome("babad")).toEqual("bab");
    expect(longestPalindrome("cbbd")).toEqual("bb");
  });

  it("evaluates isPalindrome correctly", () => {
    expect(isPalindrome("abba")).toEqual(true);
    expect(isPalindrome("abcba")).toEqual(true);
    expect(isPalindrome("a")).toEqual(true);
    expect(isPalindrome("")).toEqual(true);
    expect(isPalindrome("abc")).toEqual(false);
  });
});
