/*
 * @lc app=leetcode.cn id=706 lang=typescript
 *
 * [706] 设计哈希映射
 *
 * https://leetcode.cn/problems/design-hashmap/description/
 *
 * algorithms
 * Easy (63.91%)
 * Likes:    303
 * Dislikes: 0
 * Total Accepted:    78.8K
 * Total Submissions: 123.2K
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

// @lc code=start
class HashNode {
  constructor(
    public readonly key: number,
    public value: number,
    public prev?: HashNode,
    public next?: HashNode,
  ) {}
}

const SIZE = 10 ** 4

class MyHashMap {
  private readonly heads = new Array(SIZE).fill(0).map(() => new HashNode(-1, -1))

  private getNode(key: number) {
    const hash = key % SIZE

    let curr: HashNode | undefined = this.heads[hash]
    while (curr) {
      if (curr.key === key) {
        return curr
      }
      curr = curr.next
    }

    return undefined
  }

  put(key: number, value: number): void {
    const hash = key % SIZE
    let node = this.getNode(key)

    if (node) {
      node.value = value
      return
    }

    node = new HashNode(key, value)
    const prev = this.heads[hash]
    const next = prev.next

    node.prev = prev
    node.next = next

    prev.next = node
    if (next) {
      next.prev = node
    }
  }

  get(key: number): number {
    const node = this.getNode(key)

    if (node) return node?.value
    return -1
  }

  remove(key: number): void {
    const node = this.getNode(key)
    if (!node) return

    const prev = node.prev, next = node.next
    if (prev) {
      prev.next = next
    }
    if (next) {
      next.prev = prev
    }
  }
}
// @lc code=end
