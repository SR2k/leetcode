import { largestRectangleArea } from '../84.柱状图中最大的矩形'

describe('84.柱状图中最大的矩形', () => {
  it('should work', () => {
    expect(largestRectangleArea([2, 1, 5, 6, 2, 3]))
      .toBe(10)
    expect(largestRectangleArea([2, 4]))
      .toBe(4)
    expect(largestRectangleArea([999,999,999,999]))
      .toBe(3996)
  })
})
