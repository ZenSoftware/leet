export function mergeSort(elements: number[]): number[] {
  if (elements.length <= 1) return elements;
  const mid = Math.floor(elements.length / 2);
  const left = mergeSort(elements.slice(0, mid));
  const right = mergeSort(elements.slice(mid));
  return merge(left, right);
}

export function merge(left: number[], right: number[]): number[] {
  const result: number[] = [];
  let l = 0;
  let r = 0;

  while (l < left.length && r < right.length) {
    if (left[l] < right[r]) {
      result.push(left[l]);
      l++;
    } else {
      result.push(right[r]);
      r++;
    }
  }

  return result.concat(left.slice(l)).concat(right.slice(r));
}
