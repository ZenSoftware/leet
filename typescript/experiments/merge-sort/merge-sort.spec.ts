import { mergeSort, merge } from './merge-sort';

describe('Merge Sort', () => {
  it('sorts correctly', () => {
    for (let i = 0; i < 100; i++) {
      const input = getAscendingArray(10);
      const solution = [...input];
      shuffle(input);
      expect(mergeSort(input)).toEqual(solution);
    }
  });

  it('merges correctly', () => {
    const left = [2, 4, 6];
    const right = [1, 3, 5];
    expect(merge(left, right)).toEqual([1, 2, 3, 4, 5, 6]);
  });
});

function getAscendingArray(size: number): number[] {
  const result = Array<number>(size);
  for (let i = 0; i < size; i++) {
    result[i] = i + 1;
  }
  return result;
}

function shuffle(elements: number[]): number[] {
  for (let i1 = 0; i1 < elements.length; i1++) {
    let i2: number;

    do {
      i2 = Math.floor(Math.random() * elements.length);
    } while (i1 === i2);

    [elements[i1], elements[i2]] = [elements[i2], elements[i1]];
  }

  return elements;
}
