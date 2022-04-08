import { longestCommonPrefix } from '../14.最长公共前缀'

describe('14.最长公共前缀', () => {
  it('should work', () => {
    expect(longestCommonPrefix(['flower', 'flow', 'flight'])).toBe('fl')
    expect(longestCommonPrefix(['dog', 'racecar', 'car'])).toBe('')
  })
})
