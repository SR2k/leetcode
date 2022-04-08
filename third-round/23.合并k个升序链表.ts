/*
 * @lc app=leetcode.cn id=23 lang=typescript
 *
 * [23] 合并K个升序链表
 *
 * https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
 *
 * algorithms
 * Hard (56.45%)
 * Likes:    1757
 * Dislikes: 0
 * Total Accepted:    394.6K
 * Total Submissions: 698.7K
 * Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
 *
 * 给你一个链表数组，每个链表都已经按升序排列。
 *
 * 请你将所有链表合并到一个升序链表中，返回合并后的链表。
 *
 *
 *
 * 示例 1：
 *
 * 输入：lists = [[1,4,5],[1,3,4],[2,6]]
 * 输出：[1,1,2,3,4,4,5,6]
 * 解释：链表数组如下：
 * [
 * ⁠ 1->4->5,
 * ⁠ 1->3->4,
 * ⁠ 2->6
 * ]
 * 将它们合并到一个有序链表中得到。
 * 1->1->2->3->4->4->5->6
 *
 *
 * 示例 2：
 *
 * 输入：lists = []
 * 输出：[]
 *
 *
 * 示例 3：
 *
 * 输入：lists = [[]]
 * 输出：[]
 *
 *
 *
 *
 * 提示：
 *
 *
 * k == lists.length
 * 0 <= k <= 10^4
 * 0 <= lists[i].length <= 500
 * -10^4 <= lists[i][j] <= 10^4
 * lists[i] 按 升序 排列
 * lists[i].length 的总和不超过 10^4
 *
 *
 */

import { PriorityQueue } from '@datastructures-js/priority-queue'
import { ListNode } from './commons/list'

export
// @lc code=start
function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
  const priorityQueue = new PriorityQueue<ListNode<number>>({
    compare: (a, b) => a.val - b.val,
  })
  for (const n of lists) {
    if (n) {
      priorityQueue.enqueue(n)
    }
  }

  const dummyHead = new ListNode(-1)
  let prev = dummyHead
  while (!priorityQueue.isEmpty()) {
    const node = priorityQueue.dequeue() as ListNode<number>
    prev.next = node
    prev = node

    if (node.next) {
      priorityQueue.enqueue(node.next)
    }
  }

  return dummyHead.next
}

// FIXME: 不能提交！！！LeetCode 没得 PriorityQueue！！
// @lc code=end
