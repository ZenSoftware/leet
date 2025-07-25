import { BSTIterator, TreeNode } from './binary-search-tree-iterator';

describe('Binary Search Tree Iterator', () => {
  it('evaluates correctly', () => {
    const n7 = new TreeNode(7);
    const n3 = new TreeNode(3);
    const n15 = new TreeNode(15);
    const n9 = new TreeNode(9);
    const n20 = new TreeNode(20);

    // const root = new TreeNode(-Infinity);
    // root.right = n7;

    n7.left = n3;
    n7.right = n15;
    n15.left = n9;
    n15.right = n20;

    const bSTIterator = new BSTIterator(n7);
    expect(bSTIterator.next()).toEqual(3); // return 3
    expect(bSTIterator.next()).toEqual(7); // return 7
    expect(bSTIterator.hasNext()).toEqual(true); // return True
    expect(bSTIterator.next()).toEqual(9); // return 9
    expect(bSTIterator.hasNext()).toEqual(true); // return True
    expect(bSTIterator.next()).toEqual(15); // return 15
    expect(bSTIterator.hasNext()).toEqual(true); // return True
    expect(bSTIterator.next()).toEqual(20); // return 20
    expect(bSTIterator.hasNext()).toEqual(false); // return False
  });
});
