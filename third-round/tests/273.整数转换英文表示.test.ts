import { numberToWords } from '../273.整数转换英文表示'

describe('273.整数转换英文表示', () => {
  it('should work', () => {
    expect(numberToWords(123))
      .toBe('One Hundred Twenty Three')
    expect(numberToWords(12345))
      .toBe('Twelve Thousand Three Hundred Forty Five')
    expect(numberToWords(1234567))
      .toBe('One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven')
    expect(numberToWords(1234567891))
      .toBe('One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One')
    expect(numberToWords(100000001))
      .toBe('One Hundred Million One')
    expect(numberToWords(100000001))
      .toBe('One Hundred Million One')
    expect(numberToWords(0))
      .toBe('Zero')
  })
})
