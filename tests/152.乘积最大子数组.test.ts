import { maxProduct } from '../152.乘积最大子数组'

describe('152.乘积最大子数组', () => {
  it('should work', () => {
    expect(maxProduct([2, 3, -2, 4])).toBe(6)
    expect(maxProduct([-2, 0, -1])).toBe(0)
  })
})
