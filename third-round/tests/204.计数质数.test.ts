import { countPrimes } from '../204.计数质数'

describe('204.计数质数', () => {
  it('should work', () => {
    expect(countPrimes(10)).toBe(4)
    expect(countPrimes(0)).toBe(0)
    expect(countPrimes(1)).toBe(0)
    expect(countPrimes(10)).toBe(4)
    expect(countPrimes(999)).toBe(168)
    expect(countPrimes(9999)).toBe(1229)
    expect(countPrimes(49999)).toBe(5132)
    expect(countPrimes(5000000)).toBe(348513)
  })
})
