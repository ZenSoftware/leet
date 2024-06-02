/**
 * https://leetcode.com/problems/clone-graph/
 */
export { cloneGraph, _Node };

function cloneGraph(node: _Node | null): _Node | null {
  if (!node) return null;

  const visited = new Set<_Node>();

  function crawl(current: _Node) {
    visited.add(current);
    for (const n of current.neighbors) {
      if (!visited.has(n)) crawl(n);
    }
  }

  crawl(node);

  const nodeMap = new Map<_Node, _Node>();
  for (const n of visited) {
    const copy = new _Node(n.val);
    nodeMap.set(n, copy);
  }

  for (const n of visited) {
    const parent = nodeMap.get(n) as _Node;
    for (const a of n.neighbors) {
      const neighbor = nodeMap.get(a) as _Node;
      parent.neighbors.push(neighbor);
    }
  }

  return nodeMap.get(node) as _Node;
}

class _Node {
  val: number;
  neighbors: _Node[];

  constructor(val?: number, neighbors?: _Node[]) {
    this.val = val === undefined ? 0 : val;
    this.neighbors = neighbors === undefined ? [] : neighbors;
  }
}
