import { convert } from "./zigzag-conversion";

describe("Zigzag Conversion", () => {
  it("evaluates correctly", () => {
    expect(convert("PAYPALISHIRING", 3)).toEqual("PAHNAPLSIIGYIR");
    expect(convert("PAYPALISHIRING", 4)).toEqual("PINALSIGYAHRPI");
    expect(convert("A", 1)).toEqual("A");
    expect(convert("ABCD", 3)).toEqual("ABDC");
  });
});
