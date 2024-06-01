import { isValidBST, TreeNode } from './validate-binary-search-tree';

describe('Validate Binary Search Tree', () => {
  it('evaluates correctly', () => {
    const n1 = new TreeNode(1);
    const n2 = new TreeNode(2);
    const n3 = new TreeNode(3);
    n2.left = n1;
    n2.right = n3;
    expect(isValidBST(n2)).toEqual(true);
  });
});
