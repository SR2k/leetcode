import { maxArea } from '../11.盛最多水的容器'

describe('11.盛最多水的容器', () => {
  it('should work', () => {
    expect(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])).toBe(49)
    expect(maxArea([1, 1])).toBe(1)
  })
})
