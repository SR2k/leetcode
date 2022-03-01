import { largestNumber } from '../179.最大数'

describe('179.最大数', () => {
  it('should work', () => {
    expect(largestNumber([10, 2])).toBe('210')
    expect(largestNumber([3, 30, 34, 5, 9])).toBe('9534330')
    expect(largestNumber([1])).toBe('1')
    expect(largestNumber([10])).toBe('10')
    expect(largestNumber([0, 0])).toBe('0')
  })
})
