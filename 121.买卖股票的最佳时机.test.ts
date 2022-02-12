import { maxProfit } from './121.买卖股票的最佳时机'

describe('Best Time to Buy and Sell Stoks', () => {
  it('works', () => {
    expect(maxProfit([7, 1, 5, 3, 6, 4])).toBe(5)
    expect(maxProfit([7, 6, 4, 3, 1])).toBe(0)
    expect(maxProfit([1])).toBe(0)
  })
})
