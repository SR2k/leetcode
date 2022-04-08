import { subarraySum } from '../560.和为-k-的子数组'

describe('560.和为-k-的子数组', () => {
  it('should work', () => {
    expect(subarraySum([1, 1, 1], 2)).toBe(2)
    expect(subarraySum([1, 2, 3], 3)).toBe(2)
  })
})
