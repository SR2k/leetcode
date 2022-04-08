import { topKFrequent } from '../347.前-k-个高频元素'

describe('347.前-k-个高频元素', () => {
  it('should work', () => {
    expect(topKFrequent([5, 3, 1, 1, 1, 3, 73, 1], 1).sort())
      .toStrictEqual([1].sort())
    expect(topKFrequent([3, 0, 1, 0], 1).sort())
      .toStrictEqual([0].sort())
    expect(topKFrequent([1, 1, 1, 2, 2, 3], 2).sort())
      .toStrictEqual([1, 2].sort())
    expect(topKFrequent([1], 1).sort())
      .toStrictEqual([1].sort())
  })
})
