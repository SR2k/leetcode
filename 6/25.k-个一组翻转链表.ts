/*
 * @lc app=leetcode.cn id=25 lang=typescript
 *
 * [25] K 个一组翻转链表
 *
 * https://leetcode.cn/problems/reverse-nodes-in-k-group/description/
 *
 * algorithms
 * Hard (67.55%)
 * Likes:    1685
 * Dislikes: 0
 * Total Accepted:    358.9K
 * Total Submissions: 531.3K
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
  let curr = head

  while (curr) {
    let {
      newHead, newTail, next, count,
    } = reverse(curr, k)
    if (count < k) {
      const r = reverse(newHead!, count)
      newHead = r.newHead
      newTail = r.newTail
      next = r.next
    }

    prevEnd.next = newHead
    prevEnd = newTail
    newTail.next = null
    curr = next
  }

  return dummy.next
}

function reverse(head: ListNode, k: number) {
  let prev = null
  let curr: ListNode | null = head

  let i = 0
  for (; i < k; i++) {
    if (!curr) {
      break
    }

    const next: ListNode | null = curr.next
    curr.next = prev
    prev = curr
    curr = next
  }

  return {
    newHead: prev!,
    newTail: head,
    next: curr,
    count: i,
  }
}
// @lc code=end
