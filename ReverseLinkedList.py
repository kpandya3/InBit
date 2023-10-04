
# Definition for singly-linked list.
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head # 1
        while current is not None:
            cur_next = current.next # 
            current.next = prev
            prev = current # prev = 1
            current = cur_next # current = 2
        self.head = prev
        return prev

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
 
print ("Given linked list")
llist.printList()
llist.reverse()
print ("Reversed linked list")
llist.printList()
