import { addTwoNumbers } from '../445.两数相加-ii'
import { ListNode } from '../commons/list'

describe('445.两数相加-ii', () => {
  it('should work with immutable nodes', () => {
    expect(
      addTwoNumbers(
        ListNode.fromArray([7, 2, 4, 3]),
        ListNode.fromArray([5, 6, 4]),
      )?.toString(),
    ).toBe(ListNode.fromArray([7, 8, 0, 7])?.toString())

    expect(
      addTwoNumbers(
        ListNode.fromArray([2, 4, 3]),
        ListNode.fromArray([5, 6, 4]),
      )?.toString(),
    ).toBe(ListNode.fromArray([8, 0, 7])?.toString())

    expect(
      addTwoNumbers(
        ListNode.fromArray([0]),
        ListNode.fromArray([0]),
      )?.toString(),
    ).toBe(ListNode.fromArray([0])?.toString())

    expect(
      addTwoNumbers(
        ListNode.fromArray([9, 9, 9, 9]),
        ListNode.fromArray([1]),
      )?.toString(),
    ).toBe(ListNode.fromArray([1, 0, 0, 0, 0])?.toString())
  })
})
