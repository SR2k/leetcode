import { compress } from '../443.压缩字符串'

describe('443.压缩字符串', () => {
  it('should work', () => {
    let chars: string[]
    let result: string[]

    chars = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
    result = ['a', '2', 'b', '2', 'c', '3']
    expect(compress(chars)).toBe(result.length)
    expect(chars.slice(0, result.length)).toStrictEqual(result)

    chars = ['a']
    result = ['a']
    expect(compress(chars)).toBe(result.length)
    expect(chars.slice(0, result.length)).toStrictEqual(result)

    chars = ['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
    result = ['a', 'b', '1', '2']
    expect(compress(chars)).toBe(result.length)
    expect(chars.slice(0, result.length)).toStrictEqual(result)
  })
})
