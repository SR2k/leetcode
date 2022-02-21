import { compareVersion } from '../165.比较版本号'

describe('165.比较版本号', () => {
  it('should work', () => {
    expect(compareVersion('1.01', '1.001')).toBe(0)
    expect(compareVersion('1.0', '1.0.0')).toBe(0)
    expect(compareVersion('0.1', '1.1')).toBe(-1)
  })
})
