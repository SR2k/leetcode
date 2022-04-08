import { titleToNumber } from '../171.excel-表列序号'

describe('171.excel-表列序号', () => {
  it('should work', () => {
    expect(titleToNumber('A')).toBe(1)
    expect(titleToNumber('AB')).toBe(28)
    expect(titleToNumber('ZY')).toBe(701)
    expect(titleToNumber('FXSHRXW')).toBe(2147483647)
  })
})
