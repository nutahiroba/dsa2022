class Cell:
  def __init__(self,val) -> None:
    ##->は”アノテーション（注釈）”
    self.val = val
    self.next = None

class LinkedList:
  def __init__(self):
    ##__init__はclassを呼び出した時に呼び出される関数
    self.head = None
    self.tail = None

  def append(self,cell):
    ##cellの値を後に追加する
    if self.head == None:
      ##listの中身が空の時
      self.head = cell
      self.tail = cell
    else:
      ##それ以外の場合、後にリストを付け足す。
      self.tail.next = cell
      self.tail = cell
  
  def get(self,index):
    ##(index)番目のリストの値を取得したい
    ptr = self.head
    for i in range(0,index):
      ##0からindex番目までリストを探索
      ptr = ptr.next
      ##(index)番目の値をptrに取得
    return ptr

  def insert(self,index,cell):
    ##(index)番目に(cell)を挿入
    ptr = self.get(index-1)
    ##挿入箇所の直前のセルを指定
    if ptr.next == None:
      self.append(cell)
      ##挿入箇所の次のセルが空の場合セルを追加
    else:
      cell.next = ptr.next
      ptr.next = cell
      ##挿入箇所の次にセルがある場合、ポインタを書き換える
  
  def delete(self,cell):
    if cell.next == None:
      return
      ##後ろがからの時は何もしない。
    if cell.next.next == None:
      self.tail = cell
      ##指定したセルがtailの場合、tailを更新する
    cell.next = cell.next.next
    ##セルのポインタを更新

if __name__ == "__main__":
  linkedlist = LinkedList()
  linkedlist.append(Cell(5))
  linkedlist.append(Cell(3))
  linkedlist.append(Cell(4))
  linkedlist.append(Cell(10))
  y = linkedlist.get(3)
  linkedlist.delete(y)
  print(linkedlist.get(3).val)
