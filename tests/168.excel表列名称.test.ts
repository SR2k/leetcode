import { convertToTitle } from '../168.excel表列名称'

describe('168.excel表列名称', () => {
  it('should work', () => {
    expect(convertToTitle(1)).toBe('A')
    expect(convertToTitle(28)).toBe('AB')
    expect(convertToTitle(701)).toBe('ZY')
    expect(convertToTitle(701)).toBe('ZY')
    expect(convertToTitle(702)).toBe('ZZ')
    expect(convertToTitle(2147483647)).toBe('FXSHRXW')
  })
})
