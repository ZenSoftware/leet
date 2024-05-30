import { mergeSort as mergeSortPush } from './merge-sort';
import { mergeSort as mergeSortPreallocate } from './merge-sort-preallocate';
import { Bench } from 'tinybench';

main();

async function main() {
  const input = getShuffledArray(3000);
  const bench = new Bench({ time: 5000 });

  bench
    .add('merge sort - push', () => {
      mergeSortPush(input);
    })
    .add('merge sort - fast', () => {
      mergeSortPreallocate(input);
    });

  await bench.warmup();
  await bench.run();
  console.log(bench.table());
}

function getShuffledArray(size: number) {
  return shuffle(getAscendingArray(1000));
}

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
