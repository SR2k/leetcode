let cache

/*
 * @lc app=leetcode.cn id=146 lang=javascript
 *
 * [146] LRU 缓存机制
 *
 * https://leetcode-cn.com/problems/lru-cache/description/
 *
 * algorithms
 * Medium (52.39%)
 * Likes:    1393
 * Dislikes: 0
 * Total Accepted:    171.9K
 * Total Submissions: 327.8K
 * Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
 *
 * 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
 * 
 * 
 * 
 * 实现 LRUCache 类：
 * 
 * 
 * LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
 * int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
 * void put(int key, int value)
 * 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
 * 
 * 
 * 
 * 
 * 
 * 
 * 进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？
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
 * 1 
 * 0 
 * 0 
 * 最多调用 3 * 10^4 次 get 和 put
 * 
 * 
 */

// @lc code=start
/**
 * @param {number} capacity
 */
var LRUCache = function(capacity) {
  function HashLinkNode(key, val, prev) {
    this.val = val
    this.key = key
    this.prev = prev
  }

  // HashLinkNode.prototype.toString = function() {
  //   const ret = ['' + this.key + '_' + this.val]
  //   let next = this.next
  //   while (next) {
  //     ret.push('' + next.key + '_' + next.val)
  //     next = next.next
  //   }

  //   return ret
  // }

  this.map = {}
  this.count = 0
  this.dummy = new HashLinkNode(-1, -1)
  this.tail = this.dummy

  this.HashLinkNode = HashLinkNode
  this.capacity = capacity
};

/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
  // if (key === 3) debugger
  const node = this.map[key]
  if (!node) return -1

  this.pickToTail(node)

  // console.log('get', key, 'current cache:' + HashLinkNode.dummy.toString())

  return node.val
}

LRUCache.prototype.pickToTail = function(node) {
  if (this.tail === node) return

  node.prev.next = node.next
  node.next.prev = node.prev
  this.addToTail(node)
}

LRUCache.prototype.addToTail = function(node) {
  node.prev = this.tail
  node.next = null
  this.tail.next = node
  this.tail = node
}

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
  // if (key === 10) debugger
  const HashLinkNode = this.HashLinkNode
  let node = this.map[key]

  if (!node) {
    node = new HashLinkNode(key, value)
    if (this.capacity === this.count) {
      const head = this.dummy.next
      this.map[head.key] = null
      this.dummy.next = head.next
      if (head.next) head.next.prev = this.dummy
    } else {
      this.count++
    }
    this.addToTail(node)
    this.map[key] = node
  } else {
    node.val = value
    this.pickToTail(node)
  }

  // console.log('put', key, value, 'current cache:' + HashLinkNode.dummy.toString())
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
// @lc code=end

const cases = [
  ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"],
  [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
]

for (let i = 0; i < cases[0].length; i++) {
  switch (cases[0][i]) {
    case 'LRUCache':
      cache = new LRUCache(...cases[1][i])
      break
    case 'put':
      console.log('putting...', ...cases[1][i])
      cache.put(...cases[1][i])
      break
    case 'get':
      console.log('getting...', ...cases[1][i])
      console.log(cache.get(...cases[1][i]))
      break
  }
}
