import { LRUCache } from './146.lru-缓存'

describe('LRUCache', () => {
  let lruCache: LRUCache

  beforeEach(() => {
    lruCache = new LRUCache(3)
  })

  it('caches values when not full', () => {
    lruCache.put(1, 10)
    lruCache.put(2, 20)
    expect(lruCache.get(1)).toBe(10)
    expect(lruCache.get(2)).toBe(20)

    lruCache.put(2, 30)
    expect(lruCache.get(2)).toBe(30)
  })

  it('removed least recent used value when exceeded', () => {
    lruCache.put(1, 10)
    lruCache.put(2, 20)
    lruCache.put(3, 30)
    lruCache.put(4, 40)
    lruCache.put(5, 50)
    expect(lruCache.get(1)).toBe(-1)
    expect(lruCache.get(2)).toBe(-1)
    expect(lruCache.get(3)).toBe(30)
    expect(lruCache.get(4)).toBe(40)
    expect(lruCache.get(5)).toBe(50)
  })

  it('also treats get as use', () => {
    lruCache.put(1, 10)
    lruCache.put(2, 20)
    lruCache.put(3, 30)
    lruCache.put(4, 40)
    lruCache.put(5, 50)
    expect(lruCache.get(1)).toBe(-1)
    expect(lruCache.get(2)).toBe(-1)
    expect(lruCache.get(3)).toBe(30)

    lruCache.put(6, 60)
    expect(lruCache.get(3)).toBe(30)
    expect(lruCache.get(4)).toBe(-1)
    expect(lruCache.get(5)).toBe(50)
    expect(lruCache.get(6)).toBe(60)
  })
})
