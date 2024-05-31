/**
 * [YouTube - Learn Binary Search Tree](https://www.youtube.com/watch?v=Gt2yBZAhsGM&t=1051s)
 */
export { BinarySearchTree };

class BinarySearchTree<T = number> {
  root?: Node<T>;

  /** Constructs a tree utilizing an existing root node */
  constructor(root?: Node<T>);
  /** Constructs a tree from an array of values */
  constructor(values?: T[]);
  /** Constructs a new copy of a binary search tree */
  constructor(tree?: BinarySearchTree<T>);
  constructor(firstParam?: any) {
    if (firstParam) {
      if (Array.isArray(firstParam)) {
        for (let value of firstParam) {
          this.insert(value);
        }
      } else if (firstParam instanceof BinarySearchTree) {
        const values = firstParam.getPreOrderValues();
        for (let value of values) {
          this.insert(value);
        }
      } else {
        this.root = firstParam;
      }
    }
  }

  /**
   * Balances the tree in O(n) time
   * @returns the new root
   */
  balance() {
    const nodes = this.getInOrderNodes();

    // Reset all left and right nodes to undefined
    for (let node of nodes) {
      node.left = undefined;
      node.right = undefined;
    }

    // Recursively construct a balanced BST
    function buildTree(start: number, end: number) {
      if (start > end) return undefined;

      const mid = Math.floor((start + end) / 2);
      let node = nodes[mid];
      node.left = buildTree(start, mid - 1);
      node.right = buildTree(mid + 1, end);

      return node;
    }

    // set the new root
    this.root = buildTree(0, nodes.length - 1);

    return this.root;
  }

  insert(value: T) {
    if (!this.root) this.root = { value };
    else this.insertHelper(this.root, value);
  }

  private insertHelper(root: Node<T>, value: T) {
    if (value < root.value) {
      if (root.left) this.insertHelper(root.left, value);
      else root.left = { value };
    } else {
      if (root.right) this.insertHelper(root.right, value);
      else root.right = { value };
    }
  }

  getPreOrderValues() {
    if (!this.root) return [];
    else {
      const result: T[] = [];
      function dfs(root: Node<T>) {
        result.push(root.value);
        if (root.left) dfs(root.left);
        if (root.right) dfs(root.right);
      }
      dfs(this.root);
      return result;
    }
  }

  getInOrderValues() {
    if (!this.root) return [];
    else {
      const result: T[] = [];
      function dfs(root: Node<T>) {
        if (root.left) dfs(root.left);
        result.push(root.value);
        if (root.right) dfs(root.right);
      }
      dfs(this.root);
      return result;
    }
  }

  getInOrderNodes() {
    if (!this.root) return [];
    else {
      const result: Node<T>[] = [];
      function dfs(root: Node<T>) {
        if (root.left) dfs(root.left);
        result.push(root);
        if (root.right) dfs(root.right);
      }
      dfs(this.root);
      return result;
    }
  }
}

interface Node<T> {
  value: T;
  left?: Node<T>;
  right?: Node<T>;
}
