import { uniquePaths } from '../62.不同路径'

describe('62.不同路径', () => {
  it('should work', () => {
    expect(uniquePaths(1, 1)).toBe(1)
    expect(uniquePaths(1, 2)).toBe(1)
    expect(uniquePaths(2, 1)).toBe(1)
    expect(uniquePaths(3, 7)).toBe(28)
    expect(uniquePaths(3, 2)).toBe(3)
    expect(uniquePaths(7, 3)).toBe(28)
    expect(uniquePaths(3, 3)).toBe(6)
  })
})
