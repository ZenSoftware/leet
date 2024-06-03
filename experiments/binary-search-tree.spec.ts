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

  it('evaluates has correctly', () => {
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

  it('removes leafs correctly', () => {
    const bst = new BinarySearchTree([1, 2, 3, 4]);
    bst.remove(4);
    expect(bst.has(1)).toEqual(true);
    expect(bst.has(2)).toEqual(true);
    expect(bst.has(3)).toEqual(true);
    expect(bst.has(4)).toEqual(false);
    bst.remove(3);
    expect(bst.has(1)).toEqual(true);
    expect(bst.has(2)).toEqual(true);
    expect(bst.has(3)).toEqual(false);
    bst.remove(1);
    expect(bst.has(2)).toEqual(true);
    expect(bst.has(1)).toEqual(false);
    bst.remove(2);
    expect(bst.has(2)).toEqual(false);
  });

  it('removes node with only right branch correctly', () => {
    const bst = new BinarySearchTree();
    bst.insert(1);
    bst.insert(2);
    bst.insert(3);
    bst.insert(4);

    bst.remove(2);
    expect(bst.getInOrderValues()).toEqual([1, 3, 4]);

    bst.remove(3);
    expect(bst.getInOrderValues()).toEqual([1, 4]);

    bst.remove(1);
    expect(bst.getInOrderValues()).toEqual([4]);
  });

  it('removes node with only left branch correctly', () => {
    const bst = new BinarySearchTree();
    bst.insert(4);
    bst.insert(3);
    bst.insert(2);
    bst.insert(1);

    bst.remove(2);
    expect(bst.getInOrderValues()).toEqual([1, 3, 4]);

    bst.remove(3);
    expect(bst.getInOrderValues()).toEqual([1, 4]);

    bst.remove(4);
    expect(bst.getInOrderValues()).toEqual([1]);
  });

  it('evaluates successor correctly', () => {
    const bst = new BinarySearchTree([1, 2, 3, 4, 5, 6, 7, 8]);
    const n4 = bst.get(4);
    const successor4 = bst.successor(n4!);
    expect(successor4!.value).toEqual(5);
  });

  it('evaluates predecessor correctly', () => {
    const bst = new BinarySearchTree([1, 2, 3, 4, 5, 6, 7, 8]);
    const n4 = bst.get(4);
    const predecessor4 = bst.predecessor(n4!);
    expect(predecessor4!.value).toEqual(3);
  });

  it('removes node with left and right child correctly', () => {
    const bst = new BinarySearchTree([1, 2, 3, 4, 5, 6, 7, 8]);
    bst.remove(2);
    let after = bst.getInOrderValues();
    expect(after).toEqual([1, 3, 4, 5, 6, 7, 8]);

    bst.remove(6);
    after = bst.getInOrderValues();
    expect(after).toEqual([1, 3, 4, 5, 7, 8]);

    bst.remove(4);
    after = bst.getInOrderValues();
    expect(after).toEqual([1, 3, 5, 7, 8]);
  });

  it('Retrieves a node correctly', () => {
    const bst = new BinarySearchTree([1, 2, 3, 4, 5, 6, 7, 8]);
    const n1 = bst.get(1);
    expect(n1!.value).toEqual(1);
    const n2 = bst.get(2);
    expect(n2!.value).toEqual(2);
    const n3 = bst.get(3);
    expect(n3!.value).toEqual(3);
    const n4 = bst.get(4);
    expect(n4!.value).toEqual(4);
    const n5 = bst.get(5);
    expect(n5!.value).toEqual(5);
    const n6 = bst.get(6);
    expect(n6!.value).toEqual(6);
    const n7 = bst.get(7);
    expect(n7!.value).toEqual(7);
    const n8 = bst.get(8);
    expect(n8!.value).toEqual(8);
    const n9 = bst.get(9);
    expect(n9).toEqual(undefined);
    const n10 = bst.get(-1);
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
