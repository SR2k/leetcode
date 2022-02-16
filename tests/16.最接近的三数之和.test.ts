import { threeSumClosest } from '../16.最接近的三数之和'

describe('16. 3Sum Closest', () => {
  it('should work', () => {
    expect(threeSumClosest([0, 2, 1, -3], 1)).toBe(0)
    expect(threeSumClosest([-1, 2, 1, -4], 1)).toBe(2)
    expect(threeSumClosest([0, 0, 0], 1)).toBe(0)
  })
})
