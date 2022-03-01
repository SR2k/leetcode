import { nextGreaterElements } from '../503.下一个更大元素-ii'

describe('503.下一个更大元素-ii', () => {
  it('should work', () => {
    expect(nextGreaterElements([1, 2, 1]))
      .toStrictEqual([2, -1, 2])
    expect(nextGreaterElements([1, 2, 3, 4, 3]))
      .toStrictEqual([2, 3, 4, -1, 4])
  })
})
