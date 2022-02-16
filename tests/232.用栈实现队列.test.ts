import { MyQueue } from '../232.用栈实现队列'

describe('232.用栈实现队列', () => {
  it('should work', () => {
    const myQueue = new MyQueue()
    myQueue.push(1) // queue is: [1]
    myQueue.push(2) // queue is: [1, 2] (leftmost is front of the queue)
    expect(myQueue.peek()).toBe(1) // return 1
    expect(myQueue.pop()).toBe(1) // return 1, queue is [2]
    expect(myQueue.empty()).toBe(false) // return false
    expect(myQueue.peek()).toBe(2) // return 1
    myQueue.push(3) // [2, 3, 4]
    myQueue.push(4) // [2, 3, 4]
    expect(myQueue.pop()).toBe(2)
    expect(myQueue.pop()).toBe(3)
    expect(myQueue.empty()).toBe(false)
    expect(myQueue.pop()).toBe(4)
    expect(myQueue.empty()).toBe(true)
  })
})
