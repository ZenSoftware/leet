class MinStack:
    def __init__(self):
        self.stack = [(None, float('inf'))]

    def push(self, val: int) -> None:
        nextMin = min(val, self.stack[-1][1])
        self.stack.append((val, nextMin))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]