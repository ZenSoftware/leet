from implement_queue_using_stacks2 import MyQueue

def test1():
    myQueue = MyQueue()
    myQueue.push(1) # queue is: [1]
    myQueue.push(2) # queue is: [1, 2] (leftmost is front of the queue)
    assert myQueue.peek() == 1 # return 1
    assert myQueue.pop() == 1 # return 1, queue is [2]
    assert myQueue.empty() == False # return false