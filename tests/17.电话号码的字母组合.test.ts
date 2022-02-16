import { letterCombinations } from '../17.电话号码的字母组合'

describe('letter-combinations-of-a-phone-number', () => {
  it('works', () => {
    let query; let lc; let
      result: string[]

    query = '23'
    result = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    result.sort()
    lc = letterCombinations(query)
    lc.sort()
    expect(lc).toStrictEqual(result)

    query = ''
    result = []
    result.sort()
    lc = letterCombinations(query)
    lc.sort()
    expect(lc).toStrictEqual(result)

    query = '2'
    result = ['a', 'b', 'c']
    result.sort()
    lc = letterCombinations(query)
    lc.sort()
    expect(lc).toStrictEqual(result)
  })
})
