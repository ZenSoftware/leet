import { generateTrees, TreeNode } from './unique-binary-search-trees-ii';

describe('Unique Binary Search Trees II', () => {
  it('evaluates correctly 1', () => {
    const solution = generateTrees(3);
    expect(solution.length).toEqual(5);
  });

  it('evaluates correctly 2', () => {
    const solution = generateTrees(1);
    expect(solution.length).toEqual(1);
    expect(solution[0]!.val).toEqual(1);
  });
});
