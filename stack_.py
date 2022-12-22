class Stack:
  def __init__(self,size) -> None:
    self.size = size
    self.arr =[-1]*size
    self.top = 0

  def push(self,d):
    top = self.top
    if top == self.size-1:
      print("Overflow")
      return
    self.arr[self.top] = d
    print(self.arr)
    self.top += 1

  def pop(self):
    if self.top ==0:
      print("Underflow")
      return
    self.top -=1
    return self.arr[self.top]
  
stack = Stack(6)
stack.push(2)
stack.push(8)
stack.push(5)
stack.pop()
stack.push(4)
stack.pop()
stack.pop()
stack.push(7)
stack.push(6)
