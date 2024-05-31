/**
 * [YouTube - Learn Binary Search Tree](https://www.youtube.com/watch?v=Gt2yBZAhsGM&t=1051s)
 */
export { BinarySearchTree };

class BinarySearchTree<T = number> {
  constructor(public root?: Node<T>) {}

  insert(value: T) {
    if (!this.root) this.root = { value };
    else this.insertHelper(this.root, value);
  }

  insertHelper(root: Node<T>, value: T) {
    if (value < root.value) {
      if (root.left) this.insertHelper(root.left, value);
      else root.left = { value };
    } else {
      if (root.right) this.insertHelper(root.right, value);
      else root.right = { value };
    }
  }

  getInOrder() {
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
}

interface Node<T> {
  value: T;
  left?: Node<T>;
  right?: Node<T>;
}
