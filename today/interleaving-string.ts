/**
 * https://leetcode.com/problems/interleaving-string/description/
 */
export { isInterleave };

function isInterleave(s1: string, s2: string, s3: string): boolean {
  function search(i: number, j: number): boolean {
    if (i === s1.length && j === s2.length) {
      return true;
    }

    const result1 = s1[i] === s3[i + j] && search(i + 1, j);
    const result2 = s2[j] === s3[i + j] && search(i, j + 1);

    return result1 || result2;
  }

  return search(0, 0);
}
