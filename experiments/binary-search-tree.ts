/**
 * [YouTube - Learn Binary Search Tree](https://www.youtube.com/watch?v=Gt2yBZAhsGM&t=1051s)
 */
export { BinarySearchTree };

class BinarySearchTree<T = number> {
  root?: Node<T>;

  /** Utilize an existing root node */
  constructor(root?: Node<T>);
  /** Constructs a balanced BST from an array of values */
  constructor(values?: T[]);
  /** Constructs a new copy of a binary search tree */
  constructor(tree?: BinarySearchTree<T>);
  constructor(firstParam?: any) {
    if (firstParam) {
      if (Array.isArray(firstParam)) {
        this.constructBalanced(firstParam);
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

  /** Constructs a balanced BST from an array of values */
  private constructBalanced(values: T[]) {
    values.slice().sort((a, b) => <number>a - <number>b);
    const nodes: Node<T>[] = Array(values.length);
    for (let i = 0; i < values.length; i++) {
      nodes[i] = { value: values[i] };
    }
    this.balanceWith(nodes);
  }

  /** Balances the tree given a list of sorted nodes */
  private balanceWith(sortedNodes: Node<T>[]): Node<T> | undefined {
    // Reset all left and right nodes to undefined
    for (let node of sortedNodes) {
      node.left = undefined;
      node.right = undefined;
    }

    // Recursively construct a balanced BST
    function buildTree(start: number, end: number) {
      if (start > end) return undefined;

      const mid = Math.floor((start + end) / 2);
      let node = sortedNodes[mid];
      node.left = buildTree(start, mid - 1);
      node.right = buildTree(mid + 1, end);

      return node;
    }

    // set the new root
    this.root = buildTree(0, sortedNodes.length - 1);

    return this.root;
  }

  /**
   * Balances the tree in O(n) time and returns the new root
   */
  rebalance(): Node<T> | undefined {
    const nodes = this.getInOrderNodes();
    return this.balanceWith(nodes);
  }

  /** Inserts a value into the BST */
  insert(value: T) {
    if (!this.root) this.root = { value };
    else this.insertHelper(this.root, value);
  }

  /** Searches the tree to determine if the tree has the provided value */
  has(value: T): boolean {
    if (!this.root) {
      return false;
    } else {
      function dfs(root: Node<T> | undefined): boolean {
        if (!root) return false;
        if (root.value === value) return true;

        if (value < root.value) return dfs(root.left);
        else return dfs(root.right);
      }

      return dfs(this.root);
    }
  }

  /**
   * Searches the tree for the value and returns the respective node.
   * Returns `undefined` if the value does not exist.
   **/
  find(value: T): Node<T> | undefined {
    if (!this.root) {
      return undefined;
    } else {
      function dfs(root: Node<T> | undefined): Node<T> | undefined {
        if (!root) return undefined;
        if (root.value === value) return root;

        if (value < root.value) return dfs(root.left);
        else return dfs(root.right);
      }

      return dfs(this.root);
    }
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

  getPreOrderNodes() {
    if (!this.root) return [];
    else {
      const result: Node<T>[] = [];
      function dfs(root: Node<T>) {
        result.push(root);
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

  getPostOrderValues() {
    if (!this.root) return [];
    else {
      const result: T[] = [];
      function dfs(root: Node<T>) {
        if (root.left) dfs(root.left);
        if (root.right) dfs(root.right);
        result.push(root.value);
      }
      dfs(this.root);
      return result;
    }
  }

  getPostOrderNodes() {
    if (!this.root) return [];
    else {
      const result: Node<T>[] = [];
      function dfs(root: Node<T>) {
        if (root.left) dfs(root.left);
        if (root.right) dfs(root.right);
        result.push(root);
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
