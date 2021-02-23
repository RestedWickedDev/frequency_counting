from Node import Node

class LinkedList:

  def __init__(self):
    self.head = None


  def append(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node


  def find(self,item):

    current = self.head

    counter = 0

    for i in range(self.length()):
      if current.data.keys() == item:
        current = current.next
        counter += 1
      else:
        current = current.next

    if counter > 0:
      return counter
    else:
      return -1

    



  def length(self):
    if self.head == None:
      return 0
    else:
      counter = 1
      current = self.head
      while(current.next):
        current = current.next
        counter +=1
      return counter


  def print_nodes(self):
    current = self.head
    
    if current == None:
      print('The linked list is empty.')
    else:
      for i in range(self.length()):
        print(f'Node {i}: {current.data}')
        current = current.next

