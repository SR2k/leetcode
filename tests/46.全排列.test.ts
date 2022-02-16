import { permute } from './46.全排列'
import { mergeSorted } from './commons/utils'

describe('46. Permutations', () => {
  it('works', () => {
    expect(mergeSorted(permute([1, 2, 3])))
      .toStrictEqual(mergeSorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]))
    expect(mergeSorted(permute([1])))
      .toStrictEqual(mergeSorted([[1]]))
    expect(mergeSorted(permute([1, 2])))
      .toStrictEqual(mergeSorted([[1, 2], [2, 1]]))
  })
})
