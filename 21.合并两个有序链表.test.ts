import { mergeTwoLists } from './21.合并两个有序链表'
import { ListNode } from './commons/list'

describe('mergeTwoLists', () => {
  it('works', () => {
    expect(mergeTwoLists(ListNode.fromArray([1,2,4]), ListNode.fromArray([1,3,4]))?.toString())
      .toBe(ListNode.fromArray([1,1,2,3,4,4])?.toString())
    expect(mergeTwoLists(ListNode.fromArray([1,2,4]), ListNode.fromArray([]))?.toString())
      .toBe(ListNode.fromArray([1,2,4])?.toString())
    expect(mergeTwoLists(ListNode.fromArray([]), ListNode.fromArray([1,2,4]))?.toString())
      .toBe(ListNode.fromArray([1,2,4])?.toString())
    expect(mergeTwoLists(ListNode.fromArray([]), ListNode.fromArray([]))?.toString())
      .toBe(ListNode.fromArray([])?.toString())
    expect(mergeTwoLists(ListNode.fromArray([]), ListNode.fromArray([0]))?.toString())
      .toBe(ListNode.fromArray([0])?.toString())
  })
})
