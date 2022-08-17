/*
 * @lc app=leetcode.cn id=25 lang=typescript
 *
 * [25] K 个一组翻转链表
 *
 * https://leetcode.cn/problems/reverse-nodes-in-k-group/description/
 *
 * algorithms
 * Hard (67.64%)
 * Likes:    1759
 * Dislikes: 0
 * Total Accepted:    383.3K
 * Total Submissions: 566.6K
 * Testcase Example:  '[1,2,3,4,5]\n2'
 *
 * 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
 *
 * k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
 *
 * 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：head = [1,2,3,4,5], k = 2
 * 输出：[2,1,4,3,5]
 *
 *
 * 示例 2：
 *
 *
 *
 *
 * 输入：head = [1,2,3,4,5], k = 3
 * 输出：[3,2,1,4,5]
 *
 *
 *
 * 提示：
 *
 *
 * 链表中的节点数目为 n
 * 1 <= k <= n <= 5000
 * 0 <= Node.val <= 1000
 *
 *
 *
 *
 * 进阶：你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？
 *
 *
 *
 *
 */

import { ListNode } from './commons/list'

export
// @lc code=start
function reverseKGroup(head: ListNode | null, k: number): ListNode | null {
  const dummy = new ListNode(-1, head)

  let prevEnd = dummy
  let curr = dummy.next

  while (curr) {
    let prev: ListNode | null = null
    let insufficientNode = false
    const groupEntrance = curr

    for (let i = 0; i < k; i++) {
      if (!curr) {
        insufficientNode = true
        break
      }
      [prev, curr] = reverse(prev, curr)
    }

    if (insufficientNode) {
      curr = prev
      prev = null
      while (curr) {
        [prev, curr] = reverse(prev, curr)
      }
    }

    prevEnd.next = prev
    if (!insufficientNode) {
      groupEntrance.next = curr
    }

    prevEnd = groupEntrance
  }

  return dummy.next
}

function reverse(prev: ListNode | null, curr: ListNode) {
  const next = curr.next
  curr.next = prev
  return [curr, next]
}
// @lc code=end
