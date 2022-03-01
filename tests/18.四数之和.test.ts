import { fourSum } from '../18.四数之和'
import { mergeSorted } from '../commons/utils'

describe('18.四数之和', () => {
  it('should work', () => {
    expect(mergeSorted(fourSum([1, 0, -1, 0, -2, 2], 0)))
      .toStrictEqual(mergeSorted([[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]))
    expect(mergeSorted(fourSum([2, 2, 2, 2, 2], 8)))
      .toStrictEqual(mergeSorted([[2, 2, 2, 2]]))
  })
})
