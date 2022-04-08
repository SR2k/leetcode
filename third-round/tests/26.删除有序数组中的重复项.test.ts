import { removeDuplicates } from '../26.删除有序数组中的重复项'

describe('26.删除有序数组中的重复项', () => {
  it('should work', () => {
    let arr: number[]

    arr = [1, 1, 2]
    expect(removeDuplicates(arr))
      .toBe(2)
    expect(arr.slice(0, 2))
      .toStrictEqual([1, 2])

    arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expect(removeDuplicates(arr))
      .toBe(5)
    expect(arr.slice(0, 5))
      .toStrictEqual([0, 1, 2, 3, 4])
  })
})
