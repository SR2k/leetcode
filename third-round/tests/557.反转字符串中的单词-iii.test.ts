import { reverseWords } from '../557.反转字符串中的单词-iii'

describe('557.反转字符串中的单词-iii', () => {
  it('should work', () => {
    expect(reverseWords("Let's take LeetCode contest"))
      .toBe("s'teL ekat edoCteeL tsetnoc")
    expect(reverseWords('God Ding'))
      .toBe('doG gniD')
  })
})
