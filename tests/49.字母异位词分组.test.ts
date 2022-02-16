import { groupAnagrams } from '../49.字母异位词分组'

const sorted = (arr: string[][]) => arr
  .map((x) => x.sort())
  .sort(((a, b) => (a[0] < b[0] ? -1 : 1)))

describe('49. Group Anagrams', () => {
  it('works', () => {
    expect(sorted(groupAnagrams(['ddddddddddg', 'dgggggggggg'])))
      .toStrictEqual(sorted([['dgggggggggg'], ['ddddddddddg']]))
    expect(sorted(groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])))
      .toStrictEqual(sorted([['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']]))
    expect(groupAnagrams([''])).toStrictEqual([['']])
    expect(groupAnagrams([])).toStrictEqual([])
  })
})
