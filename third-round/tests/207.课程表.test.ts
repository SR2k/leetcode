import { canFinish } from '../207.课程表'

describe('207.课程表', () => {
  it('should work', () => {
    expect(canFinish(2, [[1, 0]])).toBe(true)
    expect(canFinish(2, [[1, 0], [0, 1]])).toBe(false)
  })
})
