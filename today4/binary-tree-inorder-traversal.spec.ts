import { inorderTraversal, TreeNode } from './binary-tree-inorder-traversal';

describe('Binary Tree Inorder Traversal', () => {
  it('evaluates correctly', () => {
    const n1 = new TreeNode(1);
    const n2 = new TreeNode(2);
    const n3 = new TreeNode(3);
    n1.right = n2;
    n2.left = n3;

    expect(inorderTraversal(n1)).toEqual([1, 3, 2]);
    expect(inorderTraversal(null)).toEqual([]);
  });
});
