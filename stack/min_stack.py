class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:

        if self.stack:
            minimum = self.stack[-1][1]
        else:
            minimum = val

        if val < minimum:
            minimum = val

        self.stack.append((val, minimum))

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]