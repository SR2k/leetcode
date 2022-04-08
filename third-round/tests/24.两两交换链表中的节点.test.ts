import { swapPairs } from '../24.两两交换链表中的节点'
import { ListNode } from '../commons/list'

describe('24.两两交换链表中的节点', () => {
  it('should work', () => {
    expect(swapPairs(ListNode.fromArray([1,2,3,4,5,6,7,8]))?.toString())
      .toBe(ListNode.fromArray([2,1,4,3,6,5,8,7])?.toString())
    expect(swapPairs(ListNode.fromArray([1,2,3,4,5,6,999]))?.toString())
      .toBe(ListNode.fromArray([2,1,4,3,6,5,999])?.toString())
    expect(swapPairs(ListNode.fromArray([1,2,3,4]))?.toString())
      .toBe(ListNode.fromArray([2,1,4,3])?.toString())
    expect(swapPairs(ListNode.fromArray([1,2,3]))?.toString())
      .toBe(ListNode.fromArray([2,1,3])?.toString())
    expect(swapPairs(ListNode.fromArray([1,2]))?.toString())
      .toBe(ListNode.fromArray([2,1])?.toString())
    expect(swapPairs(ListNode.fromArray([1]))?.toString())
      .toBe(ListNode.fromArray([1])?.toString())
    expect(swapPairs(null))
      .toBeNull()
  })
})
