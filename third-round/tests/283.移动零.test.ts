import { moveZeroes } from '../283.移动零'

describe('283.移动零', () => {
  it('should work', () => {
    let nums: number[] = []

    nums = []
    moveZeroes(nums)
    expect(nums).toStrictEqual([])

    nums = [1]
    moveZeroes(nums)
    expect(nums).toStrictEqual([1])

    nums = [1, 1, 1]
    moveZeroes(nums)
    expect(nums).toStrictEqual([1, 1, 1])

    nums = [0, 0, 1]
    moveZeroes(nums)
    expect(nums).toStrictEqual([1, 0, 0])

    nums = [0, 0, 1, 0, 0]
    moveZeroes(nums)
    expect(nums).toStrictEqual([1, 0, 0, 0, 0])

    nums = [0, 1, 0, 3, 12]
    moveZeroes(nums)
    expect(nums).toStrictEqual([1, 3, 12, 0, 0])
  })
})
