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

  it('copies a BST correctly', () => {
    const bst1 = new BinarySearchTree([1, 2, 3, 4, 5, 6, 7, 8]);
    const bst2 = new BinarySearchTree(bst1);
    expect(bst1).toEqual(bst2);
    expect(bst2.root).not.toBe(bst1.root);
    expect(bst2.root!.left).not.toBe(bst1.root!.left);
    expect(bst2.root!.right).not.toBe(bst1.root!.right);
    expect(bst2.root!.left!.left).not.toBe(bst1.root!.left!.left);
    expect(bst2.root!.left!.right).not.toBe(bst1.root!.left!.right);
    expect(bst2.root!.right!.left).not.toBe(bst1.root!.right!.left);
    expect(bst2.root!.right!.right).not.toBe(bst1.root!.right!.right);
    expect(bst2.root!.right!.right!.right).not.toBe(bst1.root!.right!.right!.right);
  });

  it('searches with has correctly', () => {
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

  it('removes value correctly', () => {
    const bst = new BinarySearchTree([1, 2, 3, 4]);
    bst.remove(4);
    expect(bst.has(1)).toEqual(true);
    expect(bst.has(2)).toEqual(true);
    expect(bst.has(3)).toEqual(true);
    expect(bst.has(4)).toEqual(false);
  });

  it('searches with find correctly', () => {
    const bst = new BinarySearchTree([1, 2, 3, 4, 5, 6, 7, 8]);
    const n1 = bst.find(1);
    expect(n1!.value).toEqual(1);
    const n2 = bst.find(2);
    expect(n2!.value).toEqual(2);
    const n3 = bst.find(3);
    expect(n3!.value).toEqual(3);
    const n4 = bst.find(4);
    expect(n4!.value).toEqual(4);
    const n5 = bst.find(5);
    expect(n5!.value).toEqual(5);
    const n6 = bst.find(6);
    expect(n6!.value).toEqual(6);
    const n7 = bst.find(7);
    expect(n7!.value).toEqual(7);
    const n8 = bst.find(8);
    expect(n8!.value).toEqual(8);
    const n9 = bst.find(9);
    expect(n9).toEqual(undefined);
    const n10 = bst.find(-1);
    expect(n10).toEqual(undefined);
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
