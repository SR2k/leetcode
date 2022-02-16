import { productExceptSelf } from '../238.除自身以外数组的乘积'

describe('238.除自身以外数组的乘积', () => {
  it('should work', () => {
    expect(productExceptSelf([1, 2, 3, 4])).toStrictEqual([24, 12, 8, 6])
    expect(productExceptSelf([1, 2, 0, 4])).toStrictEqual([0, 0, 8, 0])
  })
})
