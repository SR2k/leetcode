import { combinationSum } from '../39.组合总和'
import { mergeSorted } from '../commons/utils'

describe('39.组合总和', () => {
  it('should work', () => {
    expect(mergeSorted(combinationSum([2, 3, 6, 7], 7)))
      .toStrictEqual(mergeSorted([[2, 2, 3], [7]]))
    expect(mergeSorted(combinationSum([2, 3, 5], 8)))
      .toStrictEqual(mergeSorted([[2, 2, 2, 2], [2, 3, 3], [3, 5]]))
    expect(mergeSorted(combinationSum([2], 1)))
      .toStrictEqual(mergeSorted([]))
    expect(mergeSorted(combinationSum([1], 1)))
      .toStrictEqual(mergeSorted([[1]]))
    expect(mergeSorted(combinationSum([1], 2)))
      .toStrictEqual(mergeSorted([[1, 1]]))
  })
})
