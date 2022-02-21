import { combinationSum2 } from '../40.组合总和-ii'
import { mergeSorted } from '../commons/utils'

describe('40.组合总和-ii', () => {
  it('should work', () => {
    expect(mergeSorted(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)))
      .toStrictEqual(mergeSorted([[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]))
    expect(mergeSorted(combinationSum2([2, 5, 2, 1, 2], 5)))
      .toStrictEqual(mergeSorted([[1, 2, 2], [5]]))
  })
})
