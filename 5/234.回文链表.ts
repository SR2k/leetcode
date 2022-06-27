/*
 * @lc app=leetcode.cn id=234 lang=typescript
 *
 * [234] 回文链表
 *
 * https://leetcode.cn/problems/palindrome-linked-list/description/
 *
 * algorithms
 * Easy (51.72%)
 * Likes:    1413
 * Dislikes: 0
 * Total Accepted:    445.7K
 * Total Submissions: 861.5K
 * Testcase Example:  '[1,2,2,1]'
 *
 * 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：head = [1,2,2,1]
 * 输出：true
 *
 *
 * 示例 2：
 *
 *
 * 输入：head = [1,2]
 * 输出：false
 *
 *
 *
 *
 * 提示：
 *
 *
 * 链表中节点数目在范围[1, 10^5] 内
 * 0 <= Node.val <= 9
 *
 *
 *
 *
 * 进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
 *
 */

import { ListNode } from './commons/list'

export
// @lc code=start
function isPalindrome(head: ListNode | null): boolean {
  const middle = findMiddleAndCut(head)
  const reversed = reverse(middle)
  return isSame(head, reversed)
}

function findMiddleAndCut(head: ListNode | null): ListNode | null {
  let slow = head, fast = head

  while (fast && fast.next && fast.next.next) {
    fast = fast.next.next
    slow = slow!.next
  }

  return slow!.next
}

function reverse(head: ListNode | null): ListNode | null {
  let prev = null

  while (head) {
    const next = head.next
    head.next = prev
    prev = head
    head = next
  }

  return prev
}

function isSame(l1: ListNode | null, l2: ListNode | null) {
  while (l1 && l2) {
    if (l1.val !== l2.val) {
      return false
    }
    l1 = l1.next
    l2 = l2.next
  }
  return true
}
// @lc code=end
