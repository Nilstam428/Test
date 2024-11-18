class Node:
  def __init__(self, value):
    self.head = value
    self.left = None
    self.right = None

class Tree:
  def insert(self, element):
    #case 1 if tree is empty
    new_node = Node(element)
    if self.head is None:
      self.head = new_node
      return
    # case 2 if tree is not empty
    if self.head < element
    
  def search(self, element):
    #Self. head is the entered element:
    if self.head == element:
      print(f"{element} found")
    if self.head < element:
