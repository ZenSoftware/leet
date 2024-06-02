/**
 * https://leetcode.com/problems/clone-graph/
 */
export { cloneGraph, _Node };

function cloneGraph(node: _Node | null): _Node | null {
  return null;
}

class _Node {
  val: number;
  neighbors: _Node[];

  constructor(val?: number, neighbors?: _Node[]) {
    this.val = val === undefined ? 0 : val;
    this.neighbors = neighbors === undefined ? [] : neighbors;
  }
}
