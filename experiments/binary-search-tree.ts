/**
 * [YouTube - Learn Binary Search Tree](https://www.youtube.com/watch?v=Gt2yBZAhsGM&t=1051s)
 */
export { BinarySearchTree };

class BinarySearchTree<T = number> {
  /** The root of the BST */
  root?: Node<T>;

  /** Construct a BST with a root of undefined */
  constructor();
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
        this.constructCopy(firstParam);
      } else {
        this.root = firstParam;
      }
    }
  }

  /** Construct a new copy of a BST */
  private constructCopy(bst: BinarySearchTree<T>) {
    if (!bst.root) return;

    function dfs(root: Node<T>, parent: Node<T>) {
      if (root.left) {
        parent.left = { value: root.left.value };
        dfs(root.left, parent.left);
      }

      if (root.right) {
        parent.right = { value: root.right.value };
        dfs(root.right, parent.right);
      }
    }

    const newRoot: Node<T> = { value: bst.root.value };
    dfs(bst.root, newRoot);
    this.root = newRoot;
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
    else {
      function insertHelper(root: Node<T>, value: T) {
        if (value < root.value) {
          if (root.left) insertHelper(root.left, value);
          else root.left = { value };
        } else {
          if (root.right) insertHelper(root.right, value);
          else root.right = { value };
        }
      }
      insertHelper(this.root, value);
    }
  }

  /** Searches the tree to determine if it has the provided value */
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
   * Returns the node with the provided value if it exists, otherwise return `undefined`.
   *
   * Use `has()` if you only wish to return a boolean.
   **/
  get(value: T): Node<T> | undefined {
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

  /**
   * Removes a value from the tree.
   * Returns `true` if there was a node to remove and `false` otherwise.
   **/
  remove(value: T): boolean {
    if (!this.has(value)) return false;
    this.root = this.removeHelper(value, this.root as Node<T>);
    return true;
  }

  private removeHelper(value: T, root: Node<T>): Node<T> | undefined {
    if (value === root.value) {
      if (!root.left && !root.right) {
        return undefined;
      } else if (root.left && root.right) {
        const successor = this.successor(root) as Node<T>;
        this.removeHelper(successor.value, root);
        root.value = successor.value;
      } else if (root.left && !root.right) {
        return root.left;
      } else {
        return root.right;
      }
    } else if (value < root.value) {
      root.left = this.removeHelper(value, root.left as Node<T>);
    } else {
      root.right = this.removeHelper(value, root.right as Node<T>);
    }

    return root;
  }

  /** Get the node that is just larger than the provided node */
  successor(node: Node<T>) {
    if (!node.right) return undefined;

    let pointer = node.right;
    while (pointer?.left) {
      pointer = pointer.left;
    }
    return pointer as Node<T>;
  }

  /** Get the node that is just smaller than the provided node */
  predecessor(node: Node<T>) {
    if (!node.left) return undefined;

    let pointer = node.left;
    while (pointer?.right) {
      pointer = pointer.right;
    }
    return pointer as Node<T>;
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
