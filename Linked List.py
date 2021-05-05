##Uday Patel
##Basic Linked List Implementation
##Brian Faure

class node():
    def __init__(self,data=None): # Node initialization
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = node() #head node set to new instance of node class

    def append(self, data):
        new_node = node(data) #make a new node with data
        cur = self.head
        while cur.next != None: #traverse through the linked list loop so long as next value is not none
            cur = cur.next #move to next node
        cur.next = new_node #point current pointer to this new node

    def getSize(self):
        cur = self.head
        size = 0 #initialize the size of the linked list
        while cur.next != None: #traversal
            size += 1 #running sum
            cur = cur.next #move to next node
        return size

    def display(self):
        array = [] #create empty array list
        cur_node = self.head
        while cur_node.next != None: #traverse through linked list
            cur_node = cur_node.next #move through
            array.append(cur_node.data) #put the data value in the array list
        print(array)

    def get(self,index):
        #if index >= self.length(): #check if index is out of range of array list
            #print("ERROR: out of range!")
            #return None
        cur_idx = 0
        cur_node = self.head
        while True: #forever loop
            cur_node = cur_node.next #move through the linked list
            if cur_idx == index: #when the current index is equal to user given index, return the data at that node
                return cur_node.data
            cur_idx += 1 #increment the index variable

    def erase(self,index):
        #if index >= self.length():
            #print("ERROR: out of range!")
            #return
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node #make the current node the last node
            cur_node = cur_node.next #make the current node the n+1 node
            if cur_idx == index: #when index is equal to the user input index
                last_node.next = cur_node.next #point the n-1 node to the n+1 node (skips the nth node which effectively deletes it from the linked list)
                return
            cur_idx += 1

LinkedList = LinkedList()

LinkedList.display()
LinkedList.append(1)
LinkedList.append(2)
LinkedList.display()
LinkedList.erase(1)
LinkedList.display()
print(LinkedList.get(0))



    
