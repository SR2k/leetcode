import { threeSum } from './15.三数之和'
import { deepSorted } from './commons/utils'

describe('15. 3Sum', () => {
  it('should work', () => {
    // expect(deepSorted(threeSum( [-1,0,1,2,-1,-4])))
    //   .toStrictEqual(deepSorted([[-1,-1,2],[-1,0,1]]))
    //
    // expect(deepSorted(threeSum( [-1,-1,-1,-1,0,1,2,-1,-4])))
    //   .toStrictEqual(deepSorted([[-1,-1,2],[-1,0,1]]))

    expect(deepSorted(threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4])))
      .toStrictEqual(deepSorted([[-4, 0, 4], [-4, 1, 3], [-3, -1, 4], [-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, -1, 2], [-1, 0, 1]]))

    expect(threeSum([])).toStrictEqual([])
    expect(threeSum([0])).toStrictEqual([])
  })
})
