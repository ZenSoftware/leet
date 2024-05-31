import { BinarySearchTree } from './binary-search-tree';

describe('Binary Search Tree', () => {
  it('constructs BST from array correctly', () => {
    const bst = new BinarySearchTree([5, 4, 2, 1, 6, 8, 7, 3]);
    expect(bst.getInOrderValues()).toEqual([1, 2, 3, 4, 5, 6, 7, 8]);
  });

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
    expect(bst.getInOrderValues()).toEqual([1, 2, 3, 4, 5, 6, 7, 8]);
  });

  it('balances correctly', () => {
    const bst = new BinarySearchTree();
    bst.insert(1);
    bst.insert(2);
    bst.insert(3);
    bst.insert(4);
    bst.insert(5);
    bst.insert(6);
    bst.insert(7);
    bst.insert(8);

    const allRightValues: number[] = [];
    let pointer = bst.root;
    while (pointer) {
      allRightValues.push(pointer.value);
      pointer = pointer.right;
    }
    expect(allRightValues).toEqual([1, 2, 3, 4, 5, 6, 7, 8]);

    const balancedRoot = bst.balance();
    expect(balancedRoot!.value).toEqual(4);
    expect(balancedRoot!.left!.value).toEqual(2);
    expect(balancedRoot!.right!.value).toEqual(6);
    expect(balancedRoot!.left!.left!.value).toEqual(1);
    expect(balancedRoot!.left!.right!.value).toEqual(3);
    expect(balancedRoot!.right!.left!.value).toEqual(5);
    expect(balancedRoot!.right!.right!.value).toEqual(7);
    expect(balancedRoot!.right!.right!.right!.value).toEqual(8);
  });
});
