import { nextPermutation } from '../31.下一个排列'

describe('31.下一个排列', () => {
  it('should work', () => {
    let arr: number[]

    arr = [12, 9, 20, 19]
    nextPermutation(arr)
    expect(arr).toStrictEqual([12, 19, 9, 20])

    arr = [1, 3, 2]
    nextPermutation(arr)
    expect(arr).toStrictEqual([2, 1, 3])

    arr = [1, 2, 3]
    nextPermutation(arr)
    expect(arr).toStrictEqual([1, 3, 2])

    arr = [3, 2, 1]
    nextPermutation(arr)
    expect(arr).toStrictEqual([1, 2, 3])

    arr = [1, 1, 5]
    nextPermutation(arr)
    expect(arr).toStrictEqual([1, 5, 1])

    arr = [1, 1, 5, 1, 1]
    nextPermutation(arr)
    expect(arr).toStrictEqual([1, 5, 1, 1, 1])

    arr = [1]
    nextPermutation(arr)
    expect(arr).toStrictEqual([1])
  })
})
