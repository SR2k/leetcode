import { reverse } from '../7.整数反转'

describe('7. Reverse Integer', () => {
  it('should work', () => {
    expect(reverse(123456)).toBe(654321)
    expect(reverse(-123456)).toBe(-654321)
    expect(reverse(-120005)).toBe(-500021)
    expect(reverse(120000)).toBe(21)
    expect(reverse(-0)).toBe(0)
    expect(reverse(0)).toBe(0)
  })

  it('should return 0 for exceeded results', () => {
    expect(reverse(1234567899)).toBe(0)
    expect(reverse(-1234567899)).toBe(0)

    expect(reverse(-9463847412)).toBe(0)
    expect(reverse(-8463847412)).toBe(-2147483648)

    expect(reverse(8463847412)).toBe(0)
    expect(reverse(7463847412)).toBe(2147483647)
  })
})
