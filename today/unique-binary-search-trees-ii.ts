/**
 * https://leetcode.com/problems/unique-binary-search-trees-ii/
 */
export { generateTrees, TreeNode };

function generateTrees(n: number): Array<TreeNode | null> {
  return [];
}

class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

// function permutations(n: number): number[][] {
//   function perms(remaining: number[]): number[][] {
//     if (remaining.length === 0) return [[]];

//     const firstEl = remaining[0];
//     const withoutFirst = remaining.slice(1);
//     const permsWithoutFirst = perms(withoutFirst);
//     const permsWithFirst: number[][] = [];

//     for (let perm of permsWithoutFirst) {
//       for (let i = 0; i <= perm.length; i++) {
//         permsWithFirst.push([...perm.slice(0, i), firstEl, ...perm.slice(i)]);
//       }
//     }

//     return permsWithFirst;
//   }

//   const elements: number[] = Array(n);
//   for (let i = 1; i <= n; i++) {
//     elements[i - 1] = i;
//   }

//   return perms(elements);
// }
