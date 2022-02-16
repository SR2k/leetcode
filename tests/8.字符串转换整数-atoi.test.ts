import { myAtoi } from './8.字符串转换整数-atoi'

describe('8. String to Integer (atoi)', () => {
  it('should work for valid strings', () => {
    expect(myAtoi('42')).toBe(42)
    expect(myAtoi('-42')).toBe(-42)
    expect(myAtoi('0042')).toBe(42)
    expect(myAtoi('-0042')).toBe(-42)
    expect(myAtoi('-0')).toBe(-0)
    expect(myAtoi('0')).toBe(0)
  })

  it('should work with leading spaces', () => {
    expect(myAtoi('     42')).toBe(42)
    expect(myAtoi('  -42')).toBe(-42)
    expect(myAtoi('  0042')).toBe(42)
    expect(myAtoi('       -0042')).toBe(-42)
  })

  it('should work with trailing non-digit characters', () => {
    expect(myAtoi('     42...')).toBe(42)
    expect(myAtoi('-42 abc')).toBe(-42)
    expect(myAtoi('  0042 h')).toBe(42)
    expect(myAtoi('       -0042+-+-')).toBe(-42)
  })

  it('should return edge for exceeded cases', () => {
    expect(myAtoi(String(-1 * 2 ** 31))).toBe(-1 * 2 ** 31)
    expect(myAtoi(String(2 ** 31 - 1))).toBe(2 ** 31 - 1)
    expect(myAtoi(String(-1 * 2 ** 31 - 1))).toBe(-1 * 2 ** 31)
    expect(myAtoi(String(2 ** 31))).toBe(2 ** 31 - 1)
    expect(myAtoi(String(-1 * 2 ** 31 - 10))).toBe(-1 * 2 ** 31)
    expect(myAtoi(String(2 ** 31 + 9))).toBe(2 ** 31 - 1)
  })

  it('should return 0 for invalid cases', () => {
    expect(myAtoi('aaabb')).toBe(0)
    expect(myAtoi('+a')).toBe(0)
    expect(myAtoi('')).toBe(0)
    expect(myAtoi('   + 100')).toBe(0)
    expect(myAtoi('  b + 100')).toBe(0)
  })
})
