import { multiply } from '../43.字符串相乘'

describe('43.字符串相乘', () => {
  it('should work', () => {
    expect(multiply('2', '3'))
      .toBe('6')
    expect(multiply('123', '456'))
      .toBe('56088')
    expect(multiply('947994', '5234785'))
      .toBe('4962544771290')
    expect(multiply('0', '456'))
      .toBe('0')
    expect(multiply('0', '0'))
      .toBe('0')
  })
})
