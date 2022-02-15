import { threeSumSmaller } from './259.较小的三数之和'

describe('259. 3Sum Smaller', () => {
  it('should work', () => {
    expect(threeSumSmaller([-2, 0, 1, 3], 2)).toBe(2)
    expect(threeSumSmaller([-2, -2, 0, 1, 9, 1, 3], 2)).toBe(12)
    expect(threeSumSmaller([-2, -3], -5)).toBe(0)
    expect(threeSumSmaller([-2], -5)).toBe(0)
  })
})
