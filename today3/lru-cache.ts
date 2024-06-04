/**
 * https://leetcode.com/problems/lru-cache/
 */
export { LRUCache };

class LRUCache {
  private head: CacheItem;
  private tail: CacheItem;
  private cache = new Map<number, CacheItem>();

  constructor(private capacity: number) {
    if (capacity <= 0) {
      throw Error(`LRUCache capacity must be a positive integer. Recieved: ${capacity}`);
    }

    this.head = {
      key: 'HEAD' as any,
      value: 'HEAD' as any,
      next: undefined as any,
      previous: undefined as any,
    };

    this.tail = {
      key: 'TAIL' as any,
      value: 'TAIL' as any,
      next: undefined as any,
      previous: undefined as any,
    };

    this.head.next = this.tail;
    this.tail.previous = this.head;
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
        this.cache.delete(this.tail.previous.key);
        this.tail.previous.previous.next = this.tail;
        this.tail.previous = this.tail.previous.previous;
      }

      item = { key, value, next: this.head.next, previous: this.head };
      this.cache.set(key, item);
      this.head.next.previous = item;
      this.head.next = item;
    }
  }

  private moveToFront(item: CacheItem) {
    if (item !== this.head.next) {
      item.previous.next = item.next;
      item.next.previous = item.previous;

      item.next = this.head.next;
      item.previous = this.head;

      this.head.next.previous = item;
      this.head.next = item;
    }
  }
}

interface CacheItem {
  key: number;
  value: number;
  previous: CacheItem;
  next: CacheItem;
}
