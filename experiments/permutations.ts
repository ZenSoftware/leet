function permutations(elements: any[]): any[][] {}

console.log(permutations(["a", "b", "c"]));

/**
 * Expect:
 * [
 *   [].
 *   ['a'],
 *   ['b'],
 *   ['c'],
 *   ['a', 'b'],
 *   ['a', 'c'],
 *   ['b', 'a'],
 *   ['b', 'c'],
 *   ['c', 'a'],
 *   ['c', 'b'],
 *   ['a', 'c', 'b'],
 * ]
 */
