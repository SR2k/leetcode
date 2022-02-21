import { missingNumber } from '../268.丢失的数字'

describe('268.丢失的数字', () => {
  it('should work', () => {
    expect(missingNumber([3, 0, 1])).toBe(2)
    expect(missingNumber([0, 1])).toBe(2)
    expect(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])).toBe(8)
    expect(missingNumber([0])).toBe(1)
  })
})
