import { addTwoNumbers } from '../2.两数相加'
import { ListNode } from '../commons/list'

describe('addTwoNumbers', () => {
  it('works for zeros', () => {
    expect(
      addTwoNumbers(
        ListNode.fromArray([0]),
        ListNode.fromArray([0]),
      )?.toString(),
    ).toEqual(ListNode.fromArray([0])?.toString())

    expect(
      addTwoNumbers(
        ListNode.fromArray([1, 2, 3]),
        ListNode.fromArray([0]),
      )?.toString(),
    ).toEqual(ListNode.fromArray([1, 2, 3])?.toString())

    expect(
      addTwoNumbers(
        ListNode.fromArray([0]),
        ListNode.fromArray([1, 2, 3]),
      )?.toString(),
    ).toEqual(ListNode.fromArray([1, 2, 3])?.toString())
  })

  it('works', () => {
    expect(
      addTwoNumbers(
        ListNode.fromArray([2, 4, 3]),
        ListNode.fromArray([5, 6, 4]),
      )?.toString(),
    ).toEqual(ListNode.fromArray([7, 0, 8])?.toString())
  })

  it('carries', () => {
    expect(
      addTwoNumbers(
        ListNode.fromArray([9, 9, 9, 9, 9, 9, 9]),
        ListNode.fromArray([9, 9, 9, 9]),
      )?.toString(),
    ).toEqual(ListNode.fromArray([8, 9, 9, 9, 0, 0, 0, 1])?.toString())

    expect(
      addTwoNumbers(
        ListNode.fromArray([9, 1]),
        ListNode.fromArray([2]),
      )?.toString(),
    ).toEqual(ListNode.fromArray([1, 2])?.toString())

    expect(
      addTwoNumbers(
        ListNode.fromArray([9, 9, 9]),
        ListNode.fromArray([4]),
      )?.toString(),
    ).toEqual(ListNode.fromArray([3, 0, 0, 1])?.toString())

    expect(
      addTwoNumbers(
        ListNode.fromArray([9, 9, 9]),
        ListNode.fromArray([8, 5, 4, 8, 5, 4, 5, 4]),
      )?.toString(),
    ).toEqual(ListNode.fromArray([7, 5, 4, 9, 5, 4, 5, 4])?.toString())
  })
})
