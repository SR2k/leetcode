import { searchMatrix } from '../74.搜索二维矩阵'

describe('74.搜索二维矩阵', () => {
  it('should work', () => {
    expect(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
      .toBe(true)
    expect(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
      .toBe(false)
  })
})
