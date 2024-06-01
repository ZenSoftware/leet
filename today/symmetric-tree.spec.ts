import { isSymmetric, TreeNode } from './symmetric-tree';

describe('Symmetric Tree', () => {
  it('evaluates correctly 1', () => {
    const root = new TreeNode(1);
    const l2 = new TreeNode(2);
    const r2 = new TreeNode(2);
    const l3 = new TreeNode(3);
    const r3 = new TreeNode(3);
    const l4 = new TreeNode(4);
    const r4 = new TreeNode(4);
    root.left = l2;
    root.right = r2;
    l2.left = l3;
    l2.right = l4;
    r2.left = r4;
    r3.right = r3;
    expect(isSymmetric(root)).toEqual(true);
  });

  it('evaluates correctly 2', () => {
    const root = new TreeNode(1);
    const l2 = new TreeNode(2);
    const r2 = new TreeNode(2);
    const l3 = new TreeNode(3);
    const r3 = new TreeNode(3);
    root.left = l2;
    root.right = r2;
    l2.right = l3;
    r2.right = r3;
    expect(isSymmetric(root)).toEqual(false);
  });
});
