import { mySqrt } from '../69.x-的平方根'

describe('69.x-的平方根', () => {
  it('should work', () => {
    for (let i = 0; i < 2 ** 31 - 1; i += 10000) {
      expect(mySqrt(i)).toBe(Math.floor(Math.sqrt(i)))
    }
  })
})
