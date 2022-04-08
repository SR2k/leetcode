import { rob } from '../213.打家劫舍-ii'

describe('213.打家劫舍-ii', () => {
  it('should work', () => {
    expect(rob([2, 3, 2])).toBe(3)
    expect(rob([1, 2, 3, 1])).toBe(4)
    expect(rob([1, 2, 3])).toBe(3)
  })
})
