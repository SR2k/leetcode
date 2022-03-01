import { nextGreaterElement } from '../496.下一个更大元素-i'

describe('496.下一个更大元素-i', () => {
  it('should work', () => {
    expect(nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
      .toStrictEqual([-1, 3, -1])
    expect(nextGreaterElement([2, 4], [1, 2, 3, 4]))
      .toStrictEqual([3, -1])
  })
})
