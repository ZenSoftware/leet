from implement_queue_using_stacks import MyQueue

def test1():
    myQueue = MyQueue()
    myQueue.push(1)
    myQueue.push(2)
    assert myQueue.peek() == 1
    assert myQueue.pop() == 1
    assert myQueue.empty() == False

def test2():
    myQueue = MyQueue()
    myQueue.push(1)
    myQueue.push(2)
    assert myQueue.peek() == 1
    myQueue.push(3)
    assert myQueue.peek() == 1

def test3():
    myQueue = MyQueue()
    myQueue.push(1)
    myQueue.push(8)
    assert myQueue.pop() == 1
    myQueue.push(3)
    assert myQueue.peek() == 8
    assert myQueue.pop() == 8
    myQueue.push(5)
    assert myQueue.pop() == 3