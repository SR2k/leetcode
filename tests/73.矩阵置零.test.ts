import { setZeroes } from '../73.矩阵置零'

describe('73.矩阵置零', () => {
  it('should work', () => {
    let grid: number[][]

    grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    setZeroes(grid)
    expect(grid).toStrictEqual([[1, 0, 1], [0, 0, 0], [1, 0, 1]])

    grid = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    setZeroes(grid)
    expect(grid).toStrictEqual([[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])
  })
})
