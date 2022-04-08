import { searchMatrix } from '../240.搜索二维矩阵-ii'

describe('240.搜索二维矩阵-ii', () => {
  it('should work', () => {
    expect(searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20))
      .toBe(false)
    expect(searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5))
      .toBe(true)
    expect(searchMatrix([[1, 4, 7, 11, 15]], 5))
      .toBe(false)
    expect(searchMatrix([[1, 4, 7, 11, 15]], 7))
      .toBe(true)
    expect(searchMatrix([[1], [4], [7], [11], [15]], 5))
      .toBe(false)
    expect(searchMatrix([[1], [4], [7], [11], [15]], 7))
      .toBe(true)
    expect(searchMatrix([[1]], 5))
      .toBe(false)
    expect(searchMatrix([[1]], 1))
      .toBe(true)
  })
})
