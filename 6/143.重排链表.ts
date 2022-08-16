/*
 * @lc app=leetcode.cn id=143 lang=typescript
 *
 * [143] 重排链表
 *
 * https://leetcode.cn/problems/reorder-list/description/
 *
 * algorithms
 * Medium (63.99%)
 * Likes:    950
 * Dislikes: 0
 * Total Accepted:    189.4K
 * Total Submissions: 296K
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

import { ListNode } from "./commons/list";

export
// @lc code=start
function reorderList(head: ListNode | null): void {
  const middle = findAndCutMiddle(head)
  merge(head, reverse(middle))
}

function findAndCutMiddle(head: ListNode | null) {
  let fast = head, slow = head
  while (fast && fast.next && fast.next.next) {
    fast = fast.next.next
    slow = slow!.next!
  }
  const result = slow!.next
  slow!.next = null
  return result
}

function reverse(head: ListNode | null) {
  let prev: ListNode | null = null
  let curr = head

  while (curr) {
    const next = curr.next
    curr.next = prev
    prev = curr
    curr = next
  }

  return prev
}

function merge(l1: ListNode | null, l2: ListNode | null) {
  const dummy = new ListNode(-1)
  let prev = dummy

  while (l1 && l2) {
    prev.next = l1
    l1 = l1.next
    prev = prev.next

    prev.next = l2
    l2 = l2.next
    prev = prev.next

    prev.next = null
  }

  prev.next = l1 || l2
  return dummy.next
}
// @lc code=end
