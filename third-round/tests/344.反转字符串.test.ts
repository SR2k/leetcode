import { reverseString } from '../344.反转字符串'

describe('344.反转字符串', () => {
  it('should work', () => {
    let charArr: string[]

    charArr = ['1']
    reverseString(charArr)
    expect(charArr).toStrictEqual(['1'].reverse())

    charArr = ['1', '2']
    reverseString(charArr)
    expect(charArr).toStrictEqual(['1', '2'].reverse())

    charArr = ['1', '2', '3', '4']
    reverseString(charArr)
    expect(charArr).toStrictEqual(['1', '2', '3', '4'].reverse())
  })
})
