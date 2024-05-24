import { addTwoNumbers, toList, toArray } from "./add-two-numbers";

describe("Add Two Numbers", () => {
  it("evaluates correctly 1", () => {
    const l1 = toList([2, 4, 3]);
    const l2 = toList([5, 6, 4]);
    const result = addTwoNumbers(l1, l2);
    expect(toArray(result)).toEqual([7, 0, 8]);
  });

  it("evaluates correctly 2", () => {
    const l1 = toList([0]);
    const l2 = toList([0]);
    const result = addTwoNumbers(l1, l2);
    expect(toArray(result)).toEqual([0]);
  });

  it("evaluates correctly 3", () => {
    const l1 = toList([9, 9, 9, 9, 9, 9, 9]);
    const l2 = toList([9, 9, 9, 9]);
    const result = addTwoNumbers(l1, l2);
    expect(toArray(result)).toEqual([8, 9, 9, 9, 0, 0, 0, 1]);
  });
});
