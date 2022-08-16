/*
 * @lc app=leetcode.cn id=146 lang=typescript
 *
 * [146] LRU 缓存
 *
 * https://leetcode.cn/problems/lru-cache/description/
 *
 * algorithms
 * Medium (53.18%)
 * Likes:    2340
 * Dislikes: 0
 * Total Accepted:    394.2K
 * Total Submissions: 741.3K
 * Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
 *
 * 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
 *
 * 实现 LRUCache 类：
 *
 *
 *
 *
 * LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
 * int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
 * void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组
 * key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
 *
 *
 * 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
 *
 *
 *
 *
 *
 * 示例：
 *
 *
 * 输入
 * ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
 * [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
 * 输出
 * [null, null, null, 1, null, -1, null, -1, 3, 4]
 *
 * 解释
 * LRUCache lRUCache = new LRUCache(2);
 * lRUCache.put(1, 1); // 缓存是 {1=1}
 * lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
 * lRUCache.get(1);    // 返回 1
 * lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
 * lRUCache.get(2);    // 返回 -1 (未找到)
 * lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
 * lRUCache.get(1);    // 返回 -1 (未找到)
 * lRUCache.get(3);    // 返回 3
 * lRUCache.get(4);    // 返回 4
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= capacity <= 3000
 * 0 <= key <= 10000
 * 0 <= value <= 10^5
 * 最多调用 2 * 10^5 次 get 和 put
 *
 *
 */

// @lc code=start
class CacheNode<TKey, TValue> {
  public prev!: CacheNode<TKey, TValue>

  public next!: CacheNode<TKey, TValue>

  constructor(
    public readonly key: TKey,
    public value: TValue,
  ) {
  }
}

class LRUCache {
  private readonly dummyHead = new CacheNode(-1, -1)

  private readonly dummyTail = new CacheNode(-1, -1)

  private nodeMap = new Map<number, CacheNode<number, number>>()

  private size = 0

  constructor(private readonly capacity: number) {
    this.dummyHead.next = this.dummyTail
    this.dummyTail.prev = this.dummyHead
  }

  get(key: number): number {
    const node = this.nodeMap.get(key)
    if (!node) return -1

    this.delete(node)
    this.insert(node)

    return node.value
  }

  put(key: number, value: number): void {
    const node = this.nodeMap.get(key) || new CacheNode(key, value)
    node.value = value

    this.delete(node)
    this.insert(node)

    if (this.size > this.capacity) {
      this.delete(this.dummyHead.next)
    }
  }

  private insert(node: CacheNode<number, number>) {
    if (!node || this.nodeMap.get(node.key)) {
      return
    }

    this.size += 1
    this.nodeMap.set(node.key, node)

    const prev = this.dummyTail.prev
    const next = this.dummyTail

    prev.next = node
    next.prev = node
    node.next = next
    node.prev = prev
  }

  private delete(node: CacheNode<number, number>) {
    if (!node || !this.nodeMap.get(node.key)) {
      return
    }

    this.size -= 1
    this.nodeMap.delete(node.key)

    const { prev, next } = node

    prev.next = next
    next.prev = prev
  }
}
// @lc code=end
