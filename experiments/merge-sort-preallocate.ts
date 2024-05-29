export { mergeSort, merge };

function mergeSort<T>(elements: T[]): T[] {
  if (elements.length <= 1) return elements;
  const mid = Math.floor(elements.length / 2);
  const left = mergeSort(elements.slice(0, mid));
  const right = mergeSort(elements.slice(mid));
  return merge(left, right);
}

function merge<T>(left: T[], right: T[]): T[] {
  let l = 0;
  let r = 0;
  let i = 0;
  let result = Array<T>(left.length + right.length);

  while (l < left.length && r < right.length) {
    if (left[l] < right[r]) {
      result[i] = left[l];
      l++;
    } else {
      result[i] = right[r];
      r++;
    }
    i++;
  }

  if (l < left.length) {
    while (l < left.length) {
      result[i] = left[l];
      l++;
      i++;
    }
  } else {
    while (r < right.length) {
      result[i] = right[r];
      r++;
      i++;
    }
  }

  return result;
}
