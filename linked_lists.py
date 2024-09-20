class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    #declare head
    def __init__(self, head = None):
        self.head = head

bulldog = Node("Bulldog")

chihuahua = Node("Chihuahua")
bulldog.next_node = chihuahua

german_shepard = Node("German Shepard")
chihuahua.next_node = german_shepard

#to make it developer friendly use an append method

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def append(self, node):
        #if the list is empty add elements at the begining
        if self.head == None:
            self.head = node
            return
        
        #otherwise traverse the list to find the last node
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node # this line updates last_node to be the next node in the list.

        #add the node to the end
        last_node.next_node = node


list = LinkedList()

list.append(Node("Bulldog"))

list.append(Node("Chihuahua"))

list.append(Node("German Shepard"))


        
