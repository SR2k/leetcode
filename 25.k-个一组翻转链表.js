/*
 * @lc app=leetcode.cn id=25 lang=javascript
 *
 * [25] K 个一组翻转链表
 *
 * https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
 *
 * algorithms
 * Hard (64.85%)
 * Likes:    1101
 * Dislikes: 0
 * Total Accepted:    174.5K
 * Total Submissions: 269K
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

// @lc code=start
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

const reverseNextKElements = (dummy, k) => {
  // original:
  // dummy, [n1, n2, ..., nk - 1, nk], nk + 1, ...
  // reversed:
  // dummy, [nk, nk - 1, ..., n2, n1], nk + 1, ...

  // find n1、nk + 1
  const n1 = dummy.next
  let curr = n1
  for (let i = 0; i < k; i++) {
    if (!curr) return null
    curr = curr.next
  }
  const nkPlus = curr

  // do reverse
  let x = k
  curr = n1.next
  let prev = n1

  while (x > 1 && curr) {
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
    x--
  }

  // join
  dummy.next = prev
  n1.next = nkPlus

  // return next dummy
  return n1
}

/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var reverseKGroup = function(head, k) {
  let dummy = new ListNode()
  dummy.next = head

  let prev = dummy
  while (prev) {
    prev = reverseNextKElements(prev, k)
  }

  return dummy.next
};
// @lc code=end

