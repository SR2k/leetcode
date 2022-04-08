/*
 * @lc app=leetcode.cn id=24 lang=typescript
 *
 * [24] 两两交换链表中的节点
 *
 * https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
 *
 * algorithms
 * Medium (70.51%)
 * Likes:    1208
 * Dislikes: 0
 * Total Accepted:    365K
 * Total Submissions: 517.6K
 * Testcase Example:  '[1,2,3,4]'
 *
 * 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：head = [1,2,3,4]
 * 输出：[2,1,4,3]
 *
 *
 * 示例 2：
 *
 *
 * 输入：head = []
 * 输出：[]
 *
 *
 * 示例 3：
 *
 *
 * 输入：head = [1]
 * 输出：[1]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 链表中节点的数目在范围 [0, 100] 内
 * 0 <= Node.val <= 100
 *
 *
 */

import { ListNode } from './commons/list'

export
// @lc code=start
function swapPairs(head: ListNode | null): ListNode | null {
  const dummy = new ListNode(-1, head)
  let curr: ListNode | null = dummy

  while (curr && curr.next && curr.next.next) {
    const n1: ListNode = curr.next!
    const n2: ListNode = n1.next!
    const next: ListNode | null = n2.next

    curr.next = n2
    n2.next = n1
    n1.next = next
    curr = n1
  }

  return dummy.next
}
// @lc code=end
