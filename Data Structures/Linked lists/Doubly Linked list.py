class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.prev = None
    def insert_at_beginning(self, data):
        node=Node(data,self.head,None)
        if self.head is not None:
            self.head.prev = node
        self.head=node
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        itr=self.head
        while itr:
            if itr.next is None:
                break
            else:
                itr=itr.next
        node=Node(data,None,itr)
        itr.next=node
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)
    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr=self.head
        while itr:
            if itr.next is None:
                break
            itr=itr.next
        llstr=''
        while itr:
            llstr+=str(itr.data) + ' --> '
            itr=itr.prev
        print(llstr)



    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)
    def insert_at(self,index,data):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")
        if index==0:
            self.insert_at_beginning(data)
            return
        if index == self.get_length():
            self.insert_at_end(data)
            return
        count=0
        itr=self.head
        while itr:
            if count==index:
                node=Node(data,itr,itr.prev)
                if itr.prev:
                    itr.prev.next = node
                itr.prev=node
                return
            count+=1
            itr=itr.next
    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")
        if index==0:
            self.head=self.head.next
            self.head.prev=None
            return
        count=0
        itr=self.head
        while itr:
            if count==index:
                itr.prev.next=itr.next
                if itr.next:
                    itr.next.prev=itr.prev
                return
            count+=1
            itr=itr.next
    def insert_after_value(self,data_after,data_to_insert):
        if self.head is None:
            return
        itr=self.head
        while itr:
            if itr.data==data_after:
                node=Node(data_to_insert,itr.next,itr)
                if itr.next:
                    itr.next.prev=node
                itr.next=node
                return
            itr=itr.next
    def remove_by_value(self,data):
        if self.head is None:
            return
        itr=self.head
        while itr:
            if itr.data==data:
                itr.prev.next=itr.next
                itr.next.prev=itr.prev
                return
            itr=itr.next
        



dll=doubly_linked_list()
dll.insert_at_beginning(10)
dll.insert_at_beginning(100)
dll.insert_at_beginning(50)
dll.print_forward()
dll.insert_at_end(25)
dll.print_forward()
dll.insert_at(2,45)
dll.print_forward()
dll.remove_at(2)
dll.print_forward()
dll.insert_after_value(10,15)
dll.print_forward()
dll.remove_by_value(10)
dll.print_forward()
dll.print_backward()