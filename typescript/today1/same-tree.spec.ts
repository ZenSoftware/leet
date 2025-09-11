import { isSameTree, TreeNode } from './same-tree';

describe('Same Tree', () => {
  it('evaluates correctly 1', () => {
    const n1 = new TreeNode(1);
    const n2 = new TreeNode(2);
    const n3 = new TreeNode(3);
    n1.left = n2;
    n1.right = n3;
    expect(isSameTree(n1, n1)).toEqual(true);
  });

  it('evaluates correctly 2', () => {
    const n1 = new TreeNode(1);
    const n2 = new TreeNode(2);
    n1.left = n2;

    const m1 = new TreeNode(1);
    const m2 = new TreeNode(2);
    m1.right = m2;

    expect(isSameTree(n1, m1)).toEqual(false);
  });
});
