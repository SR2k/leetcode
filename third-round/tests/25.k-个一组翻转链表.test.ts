import { reverseKGroup } from '../25.k-个一组翻转链表'
import { ListNode } from '../commons/list'

describe('25.k-个一组翻转链表', () => {
  it('should work', () => {
    expect(reverseKGroup(ListNode.fromArray([1, 2, 3, 4, 5]), 2)?.toString())
      .toBe(ListNode.fromArray([2, 1, 4, 3, 5])?.toString())
    expect(reverseKGroup(ListNode.fromArray([1, 2, 3, 4, 5]), 3)?.toString())
      .toBe(ListNode.fromArray([3, 2, 1, 4, 5])?.toString())
    expect(reverseKGroup(ListNode.fromArray([1, 2, 3, 4, 5, 6]), 2)?.toString())
      .toBe(ListNode.fromArray([2, 1, 4, 3, 6, 5])?.toString())
    expect(reverseKGroup(ListNode.fromArray([1, 2, 3, 4, 5, 6]), 3)?.toString())
      .toBe(ListNode.fromArray([3, 2, 1, 6, 5, 4])?.toString())
    expect(reverseKGroup(ListNode.fromArray([1, 2, 3, 4, 5]), 4)?.toString())
      .toBe(ListNode.fromArray([4, 3,2, 1, 5])?.toString())
    expect(reverseKGroup(ListNode.fromArray([1, 2, 3, 4, 5]), 99)?.toString())
      .toBe(ListNode.fromArray([1, 2, 3, 4, 5])?.toString())
    expect(reverseKGroup(ListNode.fromArray([1, 2, 3, 4, 5]), 1)?.toString())
      .toBe(ListNode.fromArray([1, 2, 3, 4, 5])?.toString())
    expect(reverseKGroup(ListNode.fromArray([1]), 1)?.toString())
      .toBe(ListNode.fromArray([1])?.toString())
    expect(reverseKGroup(ListNode.fromArray([1]), 2)?.toString())
      .toBe(ListNode.fromArray([1])?.toString())
  })
})
