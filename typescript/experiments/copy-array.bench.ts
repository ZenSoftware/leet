import { Bench } from 'tinybench';

main();

async function main() {
  console.log('Running benchmark...');
  const input = getAscendingArray(3000);
  const bench = new Bench({ time: 5000 });

  bench
    .add('slice to copy', () => {
      let into: any[] = input.slice();
    })
    .add('spread to copy', () => {
      let into: any[] = [...input];
    })
    .add('Array.from to copy', () => {
      let into = Array.from(input);
    })
    .add('concat to copy', () => {
      let into: any[] = (<any>[]).concat(input);
    })
    .add('map to copy', () => {
      let into: any[] = input.map(x => x);
    })
    .add('filter to copy', () => {
      let into: any[] = input.filter(() => true);
    })
    .add('reduce to copy', () => {
      let into: any[] = [];
      input.reduce((prev, cur) => into.push(cur));
    })
    .add('filter to copy', () => {
      let into: any[] = input.filter(() => true);
    });

  await bench.warmup();
  await bench.run();
  console.log(bench.table());
}

function getAscendingArray(size: number): number[] {
  const result = Array<number>(size);
  for (let i = 0; i < size; i++) {
    result[i] = i + 1;
  }
  return result;
}
