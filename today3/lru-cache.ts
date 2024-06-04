/**
 * https://leetcode.com/problems/lru-cache/
 */
export { LRUCache, CacheItem };

class LRUCache {
  dummyHead: CacheItem;
  dummyTail: CacheItem;
  cache = new Map<number, CacheItem>();

  constructor(private capacity: number) {
    if (capacity <= 0) {
      throw Error(`LRUCache capacity must be a positive integer. Recieved: ${capacity}`);
    }

    this.dummyHead = {
      key: 'HEAD' as any,
      value: 'HEAD' as any,
      next: undefined as any,
      previous: undefined as any,
    };
    this.dummyTail = {
      key: 'TAIL' as any,
      value: 'TAIL' as any,
      next: undefined as any,
      previous: undefined as any,
    };
    this.dummyHead.next = this.dummyTail;
    this.dummyTail.previous = this.dummyHead;
  }

  get(key: number): number {
    const item = this.cache.get(key);
    if (item) {
      this.moveToFront(item);
      return item.value;
    }

    return -1;
  }

  put(key: number, value: number): void {
    let item = this.cache.get(key);
    if (item) {
      item.value = value;
      this.moveToFront(item);
    } else {
      if (this.cache.size === this.capacity) {
        // remove LRU
        this.cache.delete(this.dummyTail.previous.key);
        this.dummyTail.previous.previous.next = this.dummyTail;
        this.dummyTail.previous = this.dummyTail.previous.previous;
      }

      item = { key, value, next: this.dummyHead.next, previous: this.dummyHead };
      this.cache.set(key, item);
      this.dummyHead.next.previous = item;
      this.dummyHead.next = item;
    }
  }

  moveToFront(item: CacheItem) {
    if (item !== this.dummyHead.next) {
      item.previous.next = item.next;
      item.next.previous = item.previous;

      item.next = this.dummyHead.next;
      item.previous = this.dummyHead;

      this.dummyHead.next.previous = item;
      this.dummyHead.next = item;
    }
  }

  getValuesForward(): any[] {
    let pointer: CacheItem | undefined = this.dummyHead;
    const result: any[] = [];
    while (pointer) {
      result.push(pointer.value);
      pointer = pointer.next;
    }
    return result;
  }

  getValuesBackwards(): any[] {
    let pointer: CacheItem | undefined = this.dummyTail;
    const result: any[] = [];
    while (pointer) {
      result.push(pointer.value);
      pointer = pointer.previous;
    }
    return result;
  }
}

interface CacheItem {
  key: number;
  value: number;
  previous: CacheItem;
  next: CacheItem;
}
