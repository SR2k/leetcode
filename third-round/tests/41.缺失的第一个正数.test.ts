import { firstMissingPositive } from '../41.缺失的第一个正数'

describe('41.缺失的第一个正数', () => {
  it('should work', () => {
    expect(firstMissingPositive([1, 1])).toBe(2)
    expect(firstMissingPositive([1, 2, 0])).toBe(3)
    expect(firstMissingPositive([1, 2, 3])).toBe(4)
    expect(firstMissingPositive([3, 4, -1, 1])).toBe(2)
    expect(firstMissingPositive([7, 8, 9, 11, 12])).toBe(1)
    expect(firstMissingPositive([1])).toBe(2)
    expect(firstMissingPositive([0])).toBe(1)
    expect(firstMissingPositive([999])).toBe(1)
  })
})
