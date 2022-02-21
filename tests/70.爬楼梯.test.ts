import { climbStairs } from '../70.爬楼梯'

describe('70.爬楼梯', () => {
  it('should work', () => {
    expect(climbStairs(2)).toBe(2)
    expect(climbStairs(3)).toBe(3)
    expect(climbStairs(45)).toBe(1836311903)
  })
})
