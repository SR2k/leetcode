import { minMeetingRooms } from '../253.会议室-ii'

describe('253. Meeting Rooms II', () => {
  it('should work', () => {
    expect(minMeetingRooms([[0, 30], [5, 10], [15, 20]])).toBe(2)
    expect(minMeetingRooms([[13, 15], [1, 13]])).toBe(1)
    expect(minMeetingRooms([[7, 10], [2, 4]])).toBe(1)
  })
})
