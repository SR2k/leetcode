/*
 * @lc app=leetcode.cn id=25 lang=typescript
 *
 * [25] K 个一组翻转链表
 *
 * https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
 *
 * algorithms
 * Hard (66.13%)
 * Likes:    1485
 * Dislikes: 0
 * Total Accepted:    279.3K
 * Total Submissions: 422.4K
 * Testcase Example:  '[1,2,3,4,5]\n2'
 *
 * 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
 *
 * k 是一个正整数，它的值小于或等于链表的长度。
 *
 * 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
 *
 * 进阶：
 *
 *
 * 你可以设计一个只使用常数额外空间的算法来解决此问题吗？
 * 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
 *
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
 * 输入：head = [1,2,3,4,5], k = 3
 * 输出：[3,2,1,4,5]
 *
 *
 * 示例 3：
 *
 *
 * 输入：head = [1,2,3,4,5], k = 1
 * 输出：[1,2,3,4,5]
 *
 *
 * 示例 4：
 *
 *
 * 输入：head = [1], k = 1
 * 输出：[1]
 *
 *
 *
 *
 *
 * 提示：
 *
 *
 * 列表中节点的数量在范围 sz 内
 * 1
 * 0
 * 1
 *
 *
 */

import { ListNode } from './commons/list'

export
// @lc code=start
function reverseKGroup(head: ListNode | null, k: number): ListNode | null {
  const dummy = new ListNode(-1, head)
  let prevEnd = dummy

  let findResult = findNextK(prevEnd, k)
  while (findResult) {
    const [currTail, nextBegin] = findResult
    const currHead = prevEnd.next!
    reverse(currHead, currTail)
    prevEnd.next = currTail
    currHead.next = nextBegin
    prevEnd = currHead
    findResult = findNextK(prevEnd, k)
  }

  return dummy.next
}

function findNextK(prevEnd: ListNode, k: number): [ListNode, ListNode | null] | null {
  let curr: ListNode = prevEnd, next: ListNode | null = prevEnd.next

  while (k) {
    if (!curr.next) return null

    curr = curr.next
    next = curr.next
    k -= 1
  }

  return [curr, next]
}

function reverse(begin: ListNode, end: ListNode) {
  let prev: ListNode | null = null, curr: ListNode = begin

  while (prev !== end) {
    const next = curr.next
    curr.next = prev

    prev = curr
    curr = next!
  }
}
// @lc code=end

/*

        .
-1, [1, 2, 3, 4]

prevEnd = -1

prev = 1
curr = 2
next = 3

 */

// -1, [1, 2]
