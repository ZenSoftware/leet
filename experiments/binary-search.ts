export function binarySearch(numbers: number[], target: number) {
  function bs(start: number, end: number) {
    if (numbers[start] === target) return start;
    if (numbers[end] === target) return end;
    if (start >= end) return -1;

    const mid = Math.floor((start + end) / 2);

    if (target <= numbers[mid]) return bs(start, mid);
    else return bs(mid + 1, end);
  }

  return bs(0, numbers.length - 1);
}
