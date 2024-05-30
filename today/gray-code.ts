/**
 * https://leetcode.com/problems/gray-code/description/
 */
export { grayCode };

function grayCode(n: number): number[] {
  const size = 1 << n;
  let result: number[] = Array(n);
  for (let i = 0; i < size; i++) {
    result[i] = i ^ (i >> 1);
  }
  return result;
}

/**
 * String version
 */

// function grayCode(n: number): number[] {
//   const lastIndex = 2 ** n - 1;
//   const result: number[] = [];

//   for (let i = 0; i <= lastIndex; i++) {
//     let binary = i.toString(2);
//     binary = binary.padStart(n, '0');
//     let gray = binary[0];
//     for (let j = 0; j < n - 1; j++) {
//       if (binary[j] === binary[j + 1]) {
//         gray += '0';
//       } else {
//         gray += '1';
//       }
//     }
//     const decimal = Number.parseInt(gray, 2);
//     result.push(decimal);
//   }

//   return result;
// }
