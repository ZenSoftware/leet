import { lengthOfLongestSubstring } from "./longest-substring-without-repeating-characters";

describe("Longest Substring Without Repeating Characters", () => {
  it("evaluates correctly", () => {
    expect(lengthOfLongestSubstring("abcabcbb")).toEqual(3);
    expect(lengthOfLongestSubstring("bbbbb")).toEqual(1);
    expect(lengthOfLongestSubstring("pwwkew")).toEqual(3);
    expect(lengthOfLongestSubstring("p")).toEqual(1);
    expect(lengthOfLongestSubstring("au")).toEqual(2);
    expect(lengthOfLongestSubstring("bwf")).toEqual(3);
    expect(lengthOfLongestSubstring("brnk")).toEqual(4);
    expect(lengthOfLongestSubstring("")).toEqual(0);
  });
});
