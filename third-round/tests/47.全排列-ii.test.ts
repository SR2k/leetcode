import { permuteUnique } from '../47.全排列-ii'
import { mergeShallowSorted } from '../commons/utils'

describe('47.全排列-ii', () => {
  it('should work', () => {
    expect(mergeShallowSorted(permuteUnique([1, 1, 2])))
      .toStrictEqual(mergeShallowSorted([[1, 1, 2], [1, 2, 1], [2, 1, 1]]))
    expect(mergeShallowSorted(permuteUnique([1, 2, 3])))
      .toStrictEqual(mergeShallowSorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]))
    expect(permuteUnique([2, 2, 2, 2, 2]))
      .toStrictEqual([[2, 2, 2, 2, 2]])
  })
})
