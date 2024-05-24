export function binarySearch(numbers: number[], find: number) {
  function bs(start: number, end: number) {
    if (numbers[start] === find) return start;
    if (numbers[end] === find) return end;
    if (start >= end) return -1;

    const mid = Math.floor((start + end) / 2);

    if (find <= numbers[mid]) return bs(start, mid);
    else return bs(mid + 1, end);
  }

  return bs(0, numbers.length - 1);
}
