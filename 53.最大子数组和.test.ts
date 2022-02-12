import { maxSubArray } from './53.最大子数组和'

describe('maxSubArray', () => {
  it('works', () => {
    expect(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])).toBe(6)
    expect(maxSubArray([1])).toBe(1)
    expect(maxSubArray([5, 4, -1, 7, 8])).toBe(23)
  })
})
