export function binarySearch(list: number[], find: number) {
  function bs(start: number, end: number) {
    if (list[start] === find) return start;
    if (list[end] === find) return end;
    if (start >= end) return -1;

    const mid = Math.floor((start + end) / 2);

    if (find <= list[mid]) return bs(0, mid);
    else return bs(mid + 1, end);
  }
  return bs(0, list.length - 1);
}
