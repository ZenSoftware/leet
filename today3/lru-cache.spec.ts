import { LRUCache, CacheItem } from './lru-cache';

describe('LRU Cache', () => {
  it('evaluates correctly', () => {
    const lRUCache = new LRUCache(2);

    lRUCache.put(1, 1); // cache is {1=1}
    expect(lRUCache.getValuesForward()).toEqual(['HEAD', 1, 'TAIL']);
    expect(lRUCache.getValuesBackwards().reverse()).toEqual(['HEAD', 1, 'TAIL']);

    lRUCache.put(2, 2); // cache is {1=1, 2=2}
    expect(lRUCache.getValuesForward()).toEqual(['HEAD', 2, 1, 'TAIL']);
    expect(lRUCache.getValuesBackwards().reverse()).toEqual(['HEAD', 2, 1, 'TAIL']);

    expect(lRUCache.get(1)).toEqual(1); // return 1
    expect(lRUCache.getValuesForward()).toEqual(['HEAD', 1, 2, 'TAIL']);
    expect(lRUCache.getValuesBackwards().reverse()).toEqual(['HEAD', 1, 2, 'TAIL']);

    lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    expect(lRUCache.getValuesForward()).toEqual(['HEAD', 3, 1, 'TAIL']);
    expect(lRUCache.getValuesBackwards().reverse()).toEqual(['HEAD', 3, 1, 'TAIL']);

    expect(lRUCache.get(2)).toEqual(-1); // returns -1 (not found)

    lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    expect(lRUCache.getValuesForward()).toEqual(['HEAD', 4, 3, 'TAIL']);
    expect(lRUCache.getValuesBackwards().reverse()).toEqual(['HEAD', 4, 3, 'TAIL']);

    expect(lRUCache.get(1)).toEqual(-1); // return -1 (not found)

    expect(lRUCache.get(3)).toEqual(3); // return 3
    expect(lRUCache.getValuesForward()).toEqual(['HEAD', 3, 4, 'TAIL']);
    expect(lRUCache.getValuesBackwards().reverse()).toEqual(['HEAD', 3, 4, 'TAIL']);

    expect(lRUCache.get(4)).toEqual(4); // return 4
    expect(lRUCache.getValuesForward()).toEqual(['HEAD', 4, 3, 'TAIL']);
    expect(lRUCache.getValuesBackwards().reverse()).toEqual(['HEAD', 4, 3, 'TAIL']);
  });
});
