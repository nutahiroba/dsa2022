
class Cell():
  def __init__(self,val) -> None:
    self.val = val
    self.next = None
  
class LinkedStack():
  def __init__(self,size) -> None:
    self.top = None
    self.size = size
    self.count = 0

  def push(self,cell):
    if self.count == self.size:
      print("Overflow",cell.val)
    else:
      self.count +=1
      if self.top != None:
        cell.next = self.top
      self.top = cell
      print("push:{}".format(cell.val))

  def pop(self):
    if self.count <= 0:
      print("Underflow")
    else:
      self.count -=1
      if self.top == None:
        pass

      e = self.top
      self.top = e.next

      e.next = None
      print("pop:",e.val)
      return e


if __name__ ==  "__main__":
  linkedstack = LinkedStack(2)
  linkedstack.push(Cell(2))
  linkedstack.push(Cell(8))
  linkedstack.push (Cell(5))
  linkedstack.pop()
  linkedstack.push (Cell(4))
  linkedstack.pop()
  linkedstack.pop()
  linkedstack.pop()
  linkedstack.pop()
  linkedstack.push (Cell(7))
  linkedstack.push (Cell(6))


# class Cell():
#   def __init__(self,val) -> None:
#     self.val = val
#     self.next = None
  
# class LinkedStack():
#   def __init__(self) -> None:
#     self.top = None

#   def push(self,cell):
#     if self.top != None:
#       cell.next = self.top
#     self.top = cell

#   def pop(self):
#     if self.top == None:
#       return None

#     e = self.top
#     self.top = e.next

#     e.next = None
#     return e


# if __name__ ==  "__main__":
#   linkedstack = LinkedStack()
#   linkedstack.push(Cell(2))
#   linkedstack.push(Cell(8))
#   linkedstack.push (Cell(5))
#   print(linkedstack.pop().val)
#   linkedstack.push (Cell(4))
#   print(linkedstack.pop().val)
#   print(linkedstack.pop().val)
#   linkedstack.push (Cell(7))
#   linkedstack.push (Cell(6))
