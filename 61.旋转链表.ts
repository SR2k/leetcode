/*
 * @lc app=leetcode.cn id=61 lang=typescript
 *
 * [61] 旋转链表
 *
 * https://leetcode-cn.com/problems/rotate-list/description/
 *
 * algorithms
 * Medium (41.77%)
 * Likes:    723
 * Dislikes: 0
 * Total Accepted:    223.8K
 * Total Submissions: 535.8K
 * Testcase Example:  '[1,2,3,4,5]\n2'
 *
 * 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：head = [1,2,3,4,5], k = 2
 * 输出：[4,5,1,2,3]
 *
 *
 * 示例 2：
 *
 *
 * 输入：head = [0,1,2], k = 4
 * 输出：[2,0,1]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 链表中节点的数目在范围 [0, 500] 内
 * -100
 * 0
 *
 */

import { ListNode } from './commons/list'

export
// @lc code=start
function rotateRight(head: ListNode | null, k: number): ListNode | null {
  if (!head) return head

  const [length, tail] = getLengthAndTail(head)
  k %= length
  if (!k) return head

  const backN = cutAndGetEndK(head, k)
  tail.next = head
  return backN
}

function getLengthAndTail(head: ListNode): [number, ListNode] {
  let i = 0
  let prev: ListNode | null = null
  let curr: ListNode | null = head

  while (curr) {
    prev = curr
    curr = curr.next
    i += 1
  }

  return [i, prev!]
}

function cutAndGetEndK(head: ListNode, k: number) {
  let fast: ListNode = head
  let slow: ListNode = head

  for (let i = 0; i < k; i++) {
    fast = fast.next!
  }
  while (fast.next) {
    fast = fast.next
    slow = slow.next!
  }

  const next = slow.next
  slow.next = null
  return next
}
// @lc code=end
