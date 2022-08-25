/*
 * @lc app=leetcode.cn id=706 lang=typescript
 *
 * [706] 设计哈希映射
 *
 * https://leetcode.cn/problems/design-hashmap/description/
 *
 * algorithms
 * Easy (63.84%)
 * Likes:    320
 * Dislikes: 0
 * Total Accepted:    83.5K
 * Total Submissions: 130.8K
 * Testcase Example:  '["MyHashMap","put","put","get","get","put","get","remove","get"]\n' +
  '[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]'
 *
 * 不使用任何内建的哈希表库设计一个哈希映射（HashMap）。
 *
 * 实现 MyHashMap 类：
 *
 *
 * MyHashMap() 用空映射初始化对象
 * void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key
 * 已经存在于映射中，则更新其对应的值 value 。
 * int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
 * void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。
 *
 *
 *
 *
 * 示例：
 *
 *
 * 输入：
 * ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
 * [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
 * 输出：
 * [null, null, null, 1, -1, null, 1, null, -1]
 *
 * 解释：
 * MyHashMap myHashMap = new MyHashMap();
 * myHashMap.put(1, 1); // myHashMap 现在为 [[1,1]]
 * myHashMap.put(2, 2); // myHashMap 现在为 [[1,1], [2,2]]
 * myHashMap.get(1);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,2]]
 * myHashMap.get(3);    // 返回 -1（未找到），myHashMap 现在为 [[1,1], [2,2]]
 * myHashMap.put(2, 1); // myHashMap 现在为 [[1,1], [2,1]]（更新已有的值）
 * myHashMap.get(2);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,1]]
 * myHashMap.remove(2); // 删除键为 2 的数据，myHashMap 现在为 [[1,1]]
 * myHashMap.get(2);    // 返回 -1（未找到），myHashMap 现在为 [[1,1]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= key, value <= 10^6
 * 最多调用 10^4 次 put、get 和 remove 方法
 *
 *
 */

export
// @lc code=start
class MyHashMap {
  private readonly store: CacheNode[]

  constructor(private readonly size = 1e4) {
    this.store = new Array(size)
      .fill(null)
      .map(() => new CacheNode(-1, -1))
  }

  private hash(key: number) {
    return key % this.size
  }

  private find(key: number, createIfNotFound = false) {
    const hash = this.hash(key)
    let curr = this.store[hash].next

    while (curr && curr.key !== key) {
      curr = curr.next
    }

    if (!curr && createIfNotFound) {
      const prev = this.store[hash], next = this.store[hash].next
      curr = new CacheNode(key, -1)
      prev.next = curr
      curr.prev = prev
      curr.next = next
      if (next) {
        next.prev = curr
      }
    }

    return curr
  }

  put(key: number, value: number): void {
    const node = this.find(key, true)
    node!.value = value
  }

  get(key: number): number {
    return this.find(key)?.value ?? -1
  }

  remove(key: number): void {
    const node = this.find(key)
    if (!node) return

    const { prev, next } = node
    prev!.next = next
    if (next) {
      next.prev = prev
    }
  }
}

class CacheNode {
  constructor(
    public readonly key: number,
    public value: number,
    public prev: CacheNode | null = null,
    public next: CacheNode | null = null,
  ) {
  }
}
// @lc code=end
