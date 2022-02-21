import { isAnagram } from '../242.有效的字母异位词'

describe('242.有效的字母异位词', () => {
  it('should work', () => {
    expect(isAnagram('anagram', 'nagaram'))
      .toBe(true)
    expect(isAnagram('rat', 'car'))
      .toBe(false)
  })
})
