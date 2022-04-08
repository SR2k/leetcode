import { subsetsWithDup } from '../90.子集-ii'
import { mergeSorted } from '../commons/utils'

describe('90.子集-ii', () => {
  it('should work', () => {
    expect(mergeSorted(subsetsWithDup([1, 2, 2])))
      .toStrictEqual(mergeSorted([[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]))
    expect(mergeSorted(subsetsWithDup([0])))
      .toStrictEqual(mergeSorted([[], [0]]))
    expect(mergeSorted(subsetsWithDup([0, 0])))
      .toStrictEqual(mergeSorted([[], [0], [0, 0]]))
  })
})
