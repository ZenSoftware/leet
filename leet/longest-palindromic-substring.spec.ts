import { longestPalindrome } from "./longest-palindromic-substring";

describe("Longest Palindromic Substring", () => {
  it("evaluates longestPalindrome correctly", () => {
    expect(longestPalindrome("babad")).toEqual("bab");
    expect(longestPalindrome("cbbd")).toEqual("bb");
    expect(longestPalindrome("a")).toEqual("a");
    expect(longestPalindrome("ac")).toEqual("a");
    expect(longestPalindrome("aabbb")).toEqual("bbb");
    expect(longestPalindrome("abcccdccef")).toEqual("ccdcc");
  });
});
