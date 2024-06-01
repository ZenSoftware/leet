import { isValidBST, TreeNode } from './validate-binary-search-tree';

describe('Validate Binary Search Tree', () => {
  it('evaluates correctly 1', () => {
    const n1 = new TreeNode(1);
    const n2 = new TreeNode(2);
    const n3 = new TreeNode(3);
    n2.left = n1;
    n2.right = n3;
    expect(isValidBST(n2)).toEqual(true);
  });

  it('evaluates correctly 2', () => {
    const n1 = new TreeNode(1);
    const n3 = new TreeNode(3);
    const n4 = new TreeNode(4);
    const n5 = new TreeNode(5);
    n5.left = n1;
    n5.right = n4;
    n4.left = n3;
    n4.right = n1;
    expect(isValidBST(n5)).toEqual(false);
  });

  it('evaluates correctly 3', () => {
    const n3 = new TreeNode(3);
    const n4 = new TreeNode(4);
    const n5 = new TreeNode(5);
    const n6 = new TreeNode(6);
    const n7 = new TreeNode(7);
    n5.left = n4;
    n5.right = n6;
    n6.left = n3;
    n7.right = n7;
    expect(isValidBST(n5)).toEqual(false);
  });

  it('evaluates correctly 4', () => {
    const n32 = new TreeNode(32);
    const n26 = new TreeNode(26);
    const n47 = new TreeNode(47);
    const n19 = new TreeNode(19);
    const n56 = new TreeNode(56);
    const n27 = new TreeNode(27);
    n32.left = n26;
    n26.left = n19;
    n19.right = n27;
    n32.right = n47;
    n47.right = n56;
    expect(isValidBST(n32)).toEqual(false);
  });
});
