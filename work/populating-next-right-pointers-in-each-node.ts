/**
 * https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
 */
export { _Node, connect };

function connect(root: _Node | null): _Node | null {
  if (!root) return null;

  const map = new Map<number, _Node[]>();

  function dfs(node: _Node, level: number) {
    let levelNodes = map.get(level) as _Node[];
    if (!levelNodes) {
      levelNodes = [];
      map.set(level, levelNodes);
    }

    levelNodes.push(node);

    if (node.left) dfs(node.left, level + 1);
    if (node.right) dfs(node.right, level + 1);
  }

  dfs(root, 1);

  for (let nodes of map.values()) {
    for (let i = 0; i < nodes.length - 1; i++) {
      nodes[i].next = nodes[i + 1];
    }
  }

  return root;
}

class _Node {
  val: number;
  left: _Node | null;
  right: _Node | null;
  next: _Node | null;
  constructor(val?: number, left?: _Node, right?: _Node, next?: _Node) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
    this.next = next === undefined ? null : next;
  }
}
