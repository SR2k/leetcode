import { singleNumber } from '../136.只出现一次的数字'

describe('136.只出现一次的数字', () => {
  it('should work', () => {
    expect(singleNumber([2, 2, 1])).toBe(1)
    expect(singleNumber([4, 1, 2, 1, 2])).toBe(4)
  })
})
