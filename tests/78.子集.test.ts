import { subsets } from '../78.子集'
import { mergeSorted } from '../commons/utils'

describe('78.子集', () => {
  it('should work', () => {
    expect(mergeSorted(subsets([0])))
      .toStrictEqual(mergeSorted([[], [0]]))
    expect(mergeSorted(subsets([0, 1])))
      .toStrictEqual(mergeSorted([[], [0], [1], [0, 1]]))
    expect(mergeSorted(subsets([1, 2, 3])))
      .toStrictEqual(mergeSorted([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]))
  })
})
