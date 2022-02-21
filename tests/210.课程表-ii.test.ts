import { findOrder } from '../210.课程表-ii'

const matched = (got: number[], expected: number[][]) => {
  const gotJoint = got.join(',')
  return expected.map((x) => x.join(',')).includes(gotJoint)
}

describe('210.课程表-ii', () => {
  it('should work', () => {
    expect(matched(findOrder(2, [[1, 0]]), [[0, 1]]))
      .toBeTruthy()
    expect(matched(findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]), [[0, 2, 1, 3], [0, 1, 2, 3]]))
      .toBeTruthy()
    expect(matched(findOrder(1, []), [[0]]))
      .toBeTruthy()
  })
})
