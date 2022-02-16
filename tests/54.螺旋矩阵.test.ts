import { spiralOrder } from '../54.螺旋矩阵'

describe('spiralOrder', () => {
  it('works', () => {
    expect(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])).toStrictEqual([1, 2, 3, 6, 9, 8, 7, 4, 5])
    expect(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])).toStrictEqual([1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
    expect(spiralOrder([[1, 2, 3, 4]])).toStrictEqual([1, 2, 3, 4])
    expect(spiralOrder([[1], [2], [3], [4]])).toStrictEqual([1, 2, 3, 4])
    expect(spiralOrder([[1]])).toStrictEqual([1])
  })
})
