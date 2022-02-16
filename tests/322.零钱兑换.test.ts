import { coinChange } from './322.零钱兑换'

describe('322. Coin Change', () => {
  it('works', () => {
    expect(coinChange([1, 2, 5], 11)).toBe(3)
    expect(coinChange([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24], 9999)).toBe(-1)
    expect(coinChange([2], 3)).toBe(-1)
    expect(coinChange([1], 0)).toBe(0)
  })
})
