/*
 * @lc app=leetcode.cn id=146 lang=typescript
 *
 * [146] LRU 缓存
 *
 * https://leetcode.cn/problems/lru-cache/description/
 *
 * algorithms
 * Medium (52.89%)
 * Likes:    2230
 * Dislikes: 0
 * Total Accepted:    364.9K
 * Total Submissions: 689.3K
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

export
// @lc code=start
class LRUCache {
  private readonly head = new LRUNode(-1, -1)

  private readonly tail = new LRUNode(-1, -1)

  private size = 0

  private key2Node: Record<string, LRUNode | undefined> = {}

  constructor(
    private readonly capacity: number,
  ) {
    this.head.next = this.tail
    this.tail.prev = this.head
  }

  private appendNode(node: LRUNode | null) {
    if (!node) return
    if (this.key2Node[node.key]) return

    this.size++
    this.key2Node[node.key] = node

    const prev = this.tail.prev!, next = this.tail

    next.prev = node
    prev.next = node
    node.prev = prev
    node.next = next
  }

  private deleteNode(node: LRUNode | null) {
    if (!node) return
    if (!this.key2Node[node.key]) return

    this.key2Node[node.key] = undefined
    this.size--

    const prev = node.prev, next = node.next
    if (prev) {
      prev.next = next
    }
    if (next) {
      next.prev = prev
    }
  }

  get(key: number): number {
    const node = this.key2Node[key]
    if (!node) return -1

    this.deleteNode(node)
    this.appendNode(node)

    return node.value
  }

  put(key: number, value: number): void {
    const node: LRUNode = this.key2Node[key] || new LRUNode(key, value)
    node.value = value

    this.deleteNode(node)
    this.appendNode(node)

    if (this.size > this.capacity) {
      this.deleteNode(this.head.next)
    }
  }
}

class LRUNode {
  constructor(
    public readonly key: number,
    public value: number,
    public prev: LRUNode | null = null,
    public next: LRUNode | null = null,
  ) {
  }
}
// @lc code=end
