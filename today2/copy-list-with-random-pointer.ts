/**
 * https://leetcode.com/problems/copy-list-with-random-pointer/description/
 */
export { copyRandomList, _Node };

function copyRandomList(head: _Node | null): _Node | null {
  if (!head) return null;

  const originals = new Set<_Node>();
  let pointer: _Node | null = head;

  while (pointer) {
    originals.add(pointer);
    pointer = pointer.next;
  }

  const nodeMap = new Map<_Node, _Node>();

  for (let node of originals) {
    let copy = new _Node(node.val);
    nodeMap.set(node, copy);
  }

  pointer = head;

  while (pointer) {
    const copy = nodeMap.get(pointer) as _Node;
    if (pointer.next) copy.next = nodeMap.get(pointer.next) as _Node;
    if (pointer.random) copy.random = nodeMap.get(pointer.random) as _Node;
    pointer = pointer.next;
  }

  return nodeMap.get(head) as _Node;
}

class _Node {
  val: number;
  next: _Node | null;
  random: _Node | null;

  constructor(val?: number, next?: _Node, random?: _Node) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
    this.random = random === undefined ? null : random;
  }
}
