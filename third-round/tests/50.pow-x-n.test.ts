import { myPow } from '../50.pow-x-n'

describe('50.pow-x-n', () => {
  it('should work', () => {
    expect(Math.abs(myPow(2.00000, 10) - 1024.00000))
      .toBeLessThan(10 ** -7)
    expect(Math.abs(myPow(2.10000, 3) - 9.26100))
      .toBeLessThan(10 ** -7)
    expect(Math.abs(myPow(2.00000, -2) - 0.25000))
      .toBeLessThan(10 ** -7)
    expect(Math.abs(myPow(2.00000, 2) - 4))
      .toBeLessThan(10 ** -7)
  })
})
