/**
 * https://leetcode.com/problems/copy-list-with-random-pointer/description/
 */
export { copyRandomList, _Node };

function copyRandomList(head: _Node | null): _Node | null {
  return null;
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
