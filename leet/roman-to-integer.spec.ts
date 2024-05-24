import { romanToInt } from "./roman-to-integer";

describe("Roman to Integer", () => {
  it("evaluates correctly", () => {
    expect(romanToInt("III")).toEqual(3);
    expect(romanToInt("LVIII")).toEqual(58);
    expect(romanToInt("MCMXCIV")).toEqual(1994);
  });
});
