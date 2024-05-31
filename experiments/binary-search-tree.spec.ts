import { BinarySearchTree } from './binary-search-tree';

describe('Binary Search Tree', () => {
  it('inserts correctly', () => {
    const bst = new BinarySearchTree();
    bst.insert(6);
    bst.insert(3);
    bst.insert(1);
    bst.insert(8);
    bst.insert(4);
    bst.insert(2);
    bst.insert(7);
    bst.insert(5);
    expect(bst.getInOrder()).toEqual([1, 2, 3, 4, 5, 6, 7, 8]);
  });
});
