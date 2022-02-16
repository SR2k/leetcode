import { merge } from '../56.合并区间'

describe('56. Merge Intervals', () => {
  it('should work', () => {
    expect(merge([[1, 3], [2, 6], [8, 10], [15, 18]])).toStrictEqual([[1, 6], [8, 10], [15, 18]])
    expect(merge([[8, 10], [15, 18], [1, 3], [2, 6]])).toStrictEqual([[1, 6], [8, 10], [15, 18]])
    expect(merge([[1, 4], [4, 5]])).toStrictEqual([[1, 5]])
  })
})
