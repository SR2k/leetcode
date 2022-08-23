/*
 * @lc app=leetcode.cn id=143 lang=typescript
 *
 * [143] 重排链表
 *
 * https://leetcode.cn/problems/reorder-list/description/
 *
 * algorithms
 * Medium (64.21%)
 * Likes:    1004
 * Dislikes: 0
 * Total Accepted:    205.3K
 * Total Submissions: 319.6K
 * Testcase Example:  '[1,2,3,4]'
 *
 * 给定一个单链表 L 的头节点 head ，单链表 L 表示为：
 *
 *
 * L0 → L1 → … → Ln - 1 → Ln
 *
 *
 * 请将其重新排列后变为：
 *
 *
 * L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
 *
 * 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 *
 * 输入：head = [1,2,3,4]
 * 输出：[1,4,2,3]
 *
 * 示例 2：
 *
 *
 *
 *
 * 输入：head = [1,2,3,4,5]
 * 输出：[1,5,2,4,3]
 *
 *
 *
 * 提示：
 *
 *
 * 链表的长度范围为 [1, 5 * 10^4]
 * 1 <= node.val <= 1000
 *
 *
 */

import { ListNode } from './commons/list'

export
// @lc code=start
function reorderList(head: ListNode | null): void {
  const middle = findAndCutFromMiddle(head)
  merge(head, reverse(middle))
}

function findAndCutFromMiddle(head: ListNode) {
  let fast = head, slow = head
  while (fast?.next?.next) {
    fast = fast.next.next
    slow = slow!.next!
  }

  const result = slow.next
  slow.next = null
  return result
}

function reverse(head: ListNode | null) {
  let prev: ListNode | null = null
  while (head) {
    const { next } = head
    head.next = prev
    prev = head
    head = next
  }
  return prev
}

function merge(a: ListNode | null, b: ListNode | null) {
  const dummy = new ListNode(-1)
  let prev = dummy

  while (a && b) {
    prev.next = a
    const aNext = a.next
    a = aNext
    prev = prev.next

    prev.next = b
    const bNext = b.next
    b = bNext
    prev = prev.next
  }

  if (a) prev.next = a
  return dummy.next
}
// @lc code=end
