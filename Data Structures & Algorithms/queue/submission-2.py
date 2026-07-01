class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None

class Deque:
    
    def __init__(self):
        self.head=ListNode(-1)
        self.tail=ListNode(-1)

        self.head.next=self.tail
        self.tail.prev=self.head

    def isEmpty(self) -> bool:
        return self.head.next==self.tail
        

    def append(self, value: int) -> None:
        newnode=ListNode(value)

        newnode.next=self.tail
        newnode.prev=self.tail.prev

        self.tail.prev.next=newnode
        self.tail.prev=newnode
        

    def appendleft(self, value: int) -> None:
        newnode=ListNode(value)
        
        newnode.next=self.head.next
        newnode.prev=self.head

        self.head.next.prev=newnode
        self.head.next=newnode
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        targetNode= self.tail.prev
        val=targetNode.val
        prevnode = targetNode.prev

        prevnode.next=self.tail
        self.tail.prev=prevnode

        return val
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        targetnode = self.head.next
        value = targetnode.val

        targetnode.next.prev=self.head
        self.head.next=targetnode.next

        return value
        
