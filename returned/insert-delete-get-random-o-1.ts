/**
 * https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=study-plan-v2&envId=top-interview-150
 * Implement the RandomizedSet class:
 * RandomizedSet() Initializes the RandomizedSet object.
 * bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
 * bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
 * int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
 * You must implement the functions of the class such that each function works in average O(1) time complexity.
 */

export { RandomizedSet };

class RandomizedSet {
  map: Map<number, number>;
  elements: Array<number>;

  constructor() {
    this.map = new Map();
    this.elements = new Array();
  }

  insert(val: number): boolean {
    if (this.map.has(val)) return false;
    this.elements.push(val);
    this.map.set(val, this.elements.length - 1);
    return true;
  }

  remove(val: number): boolean {
    if (!this.map.has(val)) return false;
    const index = this.map.get(val) as number;
    this.map.set(this.elements[this.elements.length - 1], index);
    this.map.delete(val);
    this.swap(this.elements.length - 1, index);
    this.elements.pop();
    return true;
  }

  getRandom(): number {
    const index = Math.floor(this.elements.length * Math.random());
    return this.elements[index];
  }

  private swap(a: number, b: number) {
    const temp = this.elements[a];
    this.elements[a] = this.elements[b];
    this.elements[b] = temp;
  }
}
