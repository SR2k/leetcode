/*
 * @lc app=leetcode.cn id=146 lang=typescript
 *
 * [146] LRU 缓存
 *
 * https://leetcode-cn.com/problems/lru-cache/description/
 *
 * algorithms
 * Medium (52.46%)
 * Likes:    1854
 * Dislikes: 0
 * Total Accepted:    271.7K
 * Total Submissions: 517.8K
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
  private readonly dummyHead = new Node(-1, -1)

  private readonly dummyTail = new Node(-1, -1)

  private readonly cache: Record<number, Node> = {}

  private count = 0

  constructor(private capacity: number) {
    this.dummyHead.next = this.dummyTail
    this.dummyTail.prev = this.dummyHead
  }

  private deleteNode(node: Node) {
    if (node.prev) {
      node.prev!.next = node.next
    }
    if (node.next) {
      node.next!.prev = node.prev
    }
    node.prev = null
    node.next = null

    delete this.cache[node.key]
  }

  private insertToTail(node: Node) {
    const prevTail = this.dummyTail.prev

    this.dummyTail.prev = node
    node.prev = prevTail
    prevTail!.next = node
    node.next = this.dummyTail

    this.cache[node.key] = node
  }

  private moveNodeToTail(node: Node) {
    this.deleteNode(node)
    this.insertToTail(node)
  }

  get(key: number): number {
    const node = this.cache[key]
    if (!node) return -1
    this.moveNodeToTail(node)
    return node.val
  }

  put(key: number, value: number): void {
    if (this.cache[key]) {
      const node = this.cache[key]
      node.val = value
      this.moveNodeToTail(node)
      return
    }

    const node = new Node(key, value)
    this.insertToTail(node)

    if (this.count < this.capacity) {
      this.count += 1
    } else {
      const head = this.dummyHead.next!
      this.deleteNode(head)
    }
  }
}

class Node {
  constructor(public key: number, public val: number, public prev: Node | null = null, public next: Node | null = null) {}

  // public toString(): string {
  //   const result: number[] = [];
  //   const seen = new Set();

  //   let curr: Node|null = this;

  //   while (curr) {
  //     if (seen.has(curr)) {
  //       throw new Error("Circular linked list");
  //     }
  //     seen.add(curr)
  //     result.push(curr.val);
  //     curr = curr.next;
  //   }

  //   return result.join(" -> ");
  // }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
// @lc code=end
