import { intToRoman } from '../12.整数转罗马数字'

describe('12.整数转罗马数字', () => {
  it('should work', () => {
    expect(intToRoman(3)).toBe('III')
    expect(intToRoman(4)).toBe('IV')
    expect(intToRoman(9)).toBe('IX')
    expect(intToRoman(58)).toBe('LVIII')
    expect(intToRoman(1994)).toBe('MCMXCIV')
  })
})
