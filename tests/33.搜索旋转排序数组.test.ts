import { search } from '../33.搜索旋转排序数组'

describe('Search in Rotated Sorted Array', () => {
  it('works', () => {
    expect(search([4, 5, 6, 7, 0, 1, 2], 0)).toBe(4)
    expect(search([4, 5, 6, 7, 0, 1, 2], 3)).toBe(-1)
    expect(search([4, 5, 6, 7, 0, 1, 2], 4)).toBe(0)
    expect(search([4, 5, 6, 7, 0, 1, 2], 2)).toBe(6)
    expect(search([0, 1, 2, 4, 5, 6, 7], 0)).toBe(0)
    expect(search([0, 1, 2, 4, 5, 6, 7], 7)).toBe(6)
    expect(search([0, 1, 2, 4, 5, 6, 7], 4)).toBe(3)
    expect(search([1], 0)).toBe(-1)
  })
})
