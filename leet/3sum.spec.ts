import { threeSum } from "./3sum";

describe("3Sum", () => {
  it("evaluates correctly", () => {
    expect([-1, 0, 1, 2, -1, -4]).toEqual([
      [-1, -1, 2],
      [-1, 0, 1],
    ]);
    expect([0, 1, 1]).toEqual([]);
    expect([0, 0, 0]).toEqual([[0, 0, 0]]);
  });
});
