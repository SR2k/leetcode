#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#
# https://leetcode-cn.com/problems/lru-cache/description/
#
# algorithms
# Medium (52.46%)
# Likes:    1854
# Dislikes: 0
# Total Accepted:    271.7K
# Total Submissions: 517.8K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
#  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
# 
# 实现 LRUCache 类：
# 
# 
# 
# 
# LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组
# key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
# 
# 
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
# 
# 
# 
# 
# 
# 示例：
# 
# 
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= capacity <= 3000
# 0 <= key <= 10000
# 0 <= value <= 10^5
# 最多调用 2 * 10^5 次 get 和 put
# 
# 
#

# @lc code=start
from multiprocessing import dummy
from typing import Optional


class CacheNode:
    def __init__(self, value: int, prev: Optional['CacheNode'] = None, next: Optional['CacheNode'] = None) -> None:
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.dummy_head = CacheNode(-1)
        self.dummy_tail = CacheNode(-1)

        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

        self.capacity = capacity
        self.count = 0
        self.key_2_node: dict[int, CacheNode] = {}
        self.values: dict[int, int] = {}


    def delete_node(self, node: CacheNode):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev


    def add_node_to_head(self, node: CacheNode):
        prev_head = self.dummy_head.next
        self.dummy_head.next = node
        node.prev = self.dummy_head
        node.next = prev_head
        prev_head.prev = node


    def move_2_first(self, key: int):
        node = self.key_2_node[key]
        self.delete_node(node)
        self.add_node_to_head(node)


    def get(self, key: int) -> int:
        if key not in self.values:
            return -1
        self.move_2_first(key)
        return self.values[key]


    def put(self, key: int, value: int) -> None:
        self.values[key] = value

        if key not in self.key_2_node:
            self.count += 1
            self.key_2_node[key] = CacheNode(key)
            self.add_node_to_head(self.key_2_node[key])
        else:
            self.move_2_first(key)

        if self.count > self.capacity:
            node_to_pop = self.dummy_tail.prev
            self.values.pop(node_to_pop.value)
            self.key_2_node.pop(node_to_pop.value)
            self.count -= 1
            self.delete_node(node_to_pop)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end


def run(cmd, par):
    lru = None
    result = []
    for i, c in enumerate(cmd):
        if c == 'LRUCache':
            lru = LRUCache(par[i][0])
            result.append("null")
        elif c == 'put':
            lru.put(par[i][0], par[i][1])
            result.append("null")
        elif c == 'get':
            r = lru.get(par[i][0])
            print(r)
            result.append(str(r))
    print(f"[{','.join(result)}]")

cmd = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
par = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# run(cmd, par)
# [null, null, null, 1, null, -1, null, -1, 3, 4]



cmd = ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
par = [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
run(cmd, par)
#[null,null,null,null,null,null,-1,null,19,17,null,-1,null,null,null,-1,null,-1,5,-1,12,null,null,3,5,5,null,null,1,null,-1,null,30,5,30,null,null,null,-1,null,-1,24,null,null,18,null,null,null,null,-1,null,null,18,null,null,-1,null,null,null,null,null,18,null,null,-1,null,4,29,30,null,12,-1,null,null,null,null,29,null,null,null,null,17,22,18,null,null,null,-1,null,null,null,20,null,null,null,-1,18,18,null,null,null,null,20,null,null,null,null,null,null,null]
#[null,null,null,null,null,null,-1,null,19,17,null,-1,null,null,null,-1,null,-1,5,-1,12,null,null,3,5,5,null,null,1,null,-1,null,30,5,30,null,null,null,-1,null,-1,24,null,null,18,null,null,null,null,-1,null,null,18,null,null,-1,null,null,null,null,null,18,null,null,-1,null,4,29,30,null,12,-1,null,null,null,null,29,null,null,null,null,17,22,18,null,null,null,-1,null,null,null,20,null,null,null,-1,18,18,null,null,null,null,20,null,null,null,null,null,null,null]
