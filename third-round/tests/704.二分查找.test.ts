import { search } from '../704.二分查找'

describe('704.二分查找', () => {
  it('should work', () => {
    expect(search([-1, 0, 3, 5, 9, 12], 9)).toBe(4)
    expect(search([-1, 0, 3, 5, 9, 12], 2)).toBe(-1)
  })
})
