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
    expect(bst.getInOrderValues()).toEqual([1, 2, 3, 4, 5, 6, 7, 8]);
  });

  it('constructs a balanced BST from array correctly', () => {
    const bst = new BinarySearchTree([1, 2, 3, 4, 5, 6, 7, 8]);
    const root = bst.root;
    expect(root!.value).toEqual(4);
    expect(root!.left!.value).toEqual(2);
    expect(root!.right!.value).toEqual(6);
    expect(root!.left!.left!.value).toEqual(1);
    expect(root!.left!.right!.value).toEqual(3);
    expect(root!.right!.left!.value).toEqual(5);
    expect(root!.right!.right!.value).toEqual(7);
    expect(root!.right!.right!.right!.value).toEqual(8);
  });

  it('searches correctly', () => {
    const bst = new BinarySearchTree([1, 2, 3, 4, 5, 6, 7, 8]);
    expect(bst.has(1)).toEqual(true);
    expect(bst.has(2)).toEqual(true);
    expect(bst.has(3)).toEqual(true);
    expect(bst.has(4)).toEqual(true);
    expect(bst.has(5)).toEqual(true);
    expect(bst.has(6)).toEqual(true);
    expect(bst.has(7)).toEqual(true);
    expect(bst.has(8)).toEqual(true);
    expect(bst.has(9)).toEqual(false);
    expect(bst.has(-1)).toEqual(false);
  });

  it('rebalances correctly', () => {
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

    const balancedRoot = bst.rebalance();
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
