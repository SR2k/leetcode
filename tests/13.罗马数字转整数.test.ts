import { romanToInt } from './13.罗马数字转整数'

describe('13. Roman to Integer', () => {
  it('should work', () => {
    expect(romanToInt('III')).toBe(3)
    expect(romanToInt('LVIII')).toBe(58)
    expect(romanToInt('MCMXCIV')).toBe(1994)
  })
})
