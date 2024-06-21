class MyStack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        return not self.stack

    def is_full(self):
        return len(self.stack) == self.capacity

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow Error")
        return self.stack.pop(-1)

    def push(self, value):
        if self.is_full():
            raise IndexError("Stack Overflow Error")
        return self.stack.append(value)

    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[-1]


stack1 = MyStack(capacity=5)
stack1.push(1)
stack1.push(2)
print(stack1.is_full())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())
