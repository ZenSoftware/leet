import { LRUCache } from './lru-cache';

describe('LRU Cache', () => {
  it('evaluates correctly', () => {
    const cache = new LRUCache(2);

    cache.put(1, 1); // cache is {1=1}
    expect(forwards(cache)).toEqual(['HEAD', 1, 'TAIL']);
    expect(backwards(cache).reverse()).toEqual(['HEAD', 1, 'TAIL']);

    cache.put(2, 2); // cache is {1=1, 2=2}
    expect(forwards(cache)).toEqual(['HEAD', 2, 1, 'TAIL']);
    expect(backwards(cache).reverse()).toEqual(['HEAD', 2, 1, 'TAIL']);

    expect(cache.get(1)).toEqual(1); // return 1
    expect(forwards(cache)).toEqual(['HEAD', 1, 2, 'TAIL']);
    expect(backwards(cache).reverse()).toEqual(['HEAD', 1, 2, 'TAIL']);

    cache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    expect(forwards(cache)).toEqual(['HEAD', 3, 1, 'TAIL']);
    expect(backwards(cache).reverse()).toEqual(['HEAD', 3, 1, 'TAIL']);

    expect(cache.get(2)).toEqual(-1); // returns -1 (not found)

    cache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    expect(forwards(cache)).toEqual(['HEAD', 4, 3, 'TAIL']);
    expect(backwards(cache).reverse()).toEqual(['HEAD', 4, 3, 'TAIL']);

    expect(cache.get(1)).toEqual(-1); // return -1 (not found)

    expect(cache.get(3)).toEqual(3); // return 3
    expect(forwards(cache)).toEqual(['HEAD', 3, 4, 'TAIL']);
    expect(backwards(cache).reverse()).toEqual(['HEAD', 3, 4, 'TAIL']);

    expect(cache.get(4)).toEqual(4); // return 4
    expect(forwards(cache)).toEqual(['HEAD', 4, 3, 'TAIL']);
    expect(backwards(cache).reverse()).toEqual(['HEAD', 4, 3, 'TAIL']);
  });
});

function forwards(cache: LRUCache): any[] {
  let pointer = (<any>cache).head;
  const result: any[] = [];
  while (pointer) {
    result.push(pointer.value);
    pointer = pointer.next;
  }
  return result;
}

function backwards(cache: LRUCache): any[] {
  let pointer = (<any>cache).tail;
  const result: any[] = [];
  while (pointer) {
    result.push(pointer.value);
    pointer = pointer.previous;
  }
  return result;
}
