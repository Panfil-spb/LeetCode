class MyQueue:

    def __init__(self):
        self.mas = []
        

    def push(self, x: int) -> None:
        self.mas.append(x)

    def pop(self) -> int:
        num = self.mas[0]
        self.mas = self.mas[1:]
        return num

    def peek(self) -> int:
        return self.mas[0]
        

    def empty(self) -> bool:
        return len(self.mas) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()