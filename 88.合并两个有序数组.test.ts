import { merge } from './88.合并两个有序数组'

describe('88. Merge Sorted Array', () => {
  it('works for non empty arrays', () => {
    let nums1 = [1, 2, 3, 0, 0, 0]; let m = 3; let nums2 = [2, 5, 6]; let
      n = 3
    merge(nums1, m, nums2, n)
    expect(nums1).toStrictEqual([1, 2, 2, 3, 5, 6])

    nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
    m = 6
    nums2 = [1, 2, 2]
    n = 3
    merge(nums1, m, nums2, n)
    expect(nums1).toStrictEqual([-1, 0, 0, 1, 2, 2, 3, 3, 3])
  })

  it('works for empty arrays', () => {
    let nums1 = [1]; let m = 1; let nums2: number[] = []; let
      n = 0
    merge(nums1, m, nums2, n)
    expect(nums1).toStrictEqual([1])

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
    expect(nums1).toStrictEqual([1])
  })
})
