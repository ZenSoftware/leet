import { sortedArrayToBST, TreeNode } from './convert-sorted-array-to-binary-search-tree';

describe('Convert Sorted Array to Binary Search Tree', () => {
  it('evaluates correctly', () => {
    const n0 = new TreeNode(0);
    const nNeg3 = new TreeNode(-3);
    const n9 = new TreeNode(9);
    const n5 = new TreeNode(5);
    const nNeg10 = new TreeNode(-10);
    n0.left = nNeg3;
    n0.right = n9;
    nNeg3.left = nNeg10;
    n9.left = n5;
    expect(sortedArrayToBST([-10, -3, 0, 5, 9])).toEqual(n0);
  });
});
