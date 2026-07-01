class ListNode:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        
    def append(self, value: int) -> None:
        newnode = ListNode(value)

        newnode.prev=self.tail.prev
        newnode.next=self.tail

        self.tail.prev.next=newnode
        self.tail.prev = newnode
        

    def appendleft(self, value: int) -> None:
        newnode = ListNode(value)

        newnode.next = self.head.next
        newnode.prev = self.head

        self.head.next.prev=newnode
        self.head.next = newnode
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        newnode = self.tail.prev
        value = newnode.value

        self.tail.prev.prev.next=self.tail
        self.tail.prev = self.tail.prev.prev
        return value
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        newnode = self.head.next
        value = newnode.value

        
        self.head.next.next.prev=self.head
        self.head.next = self.head.next.next
        

        return value
        
