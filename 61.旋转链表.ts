/*
 * @lc app=leetcode.cn id=61 lang=typescript
 *
 * [61] 旋转链表
 *
 * https://leetcode.cn/problems/rotate-list/description/
 *
 * algorithms
 * Medium (41.65%)
 * Likes:    818
 * Dislikes: 0
 * Total Accepted:    273.4K
 * Total Submissions: 656.4K
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
 * -100 <= Node.val <= 100
 * 0 <= k <= 2 * 10^9
 *
 *
 */

import { ListNode } from './commons/list'

export
// @lc code=start
function rotateRight(head: ListNode | null, k: number): ListNode | null {
  if (!head || !k) return head

  let fast: ListNode | null = head, slow = head
  let i = k, cnt = 0
  while (fast && i--) {
    fast = fast.next
    cnt++
  }
  if (!fast) {
    return rotateRight(head, k % cnt)
  }

  while (fast.next) {
    fast = fast.next
    slow = slow.next!
  }

  const newHead = slow.next
  slow.next = null
  fast.next = head
  return newHead
}
// @lc code=end
