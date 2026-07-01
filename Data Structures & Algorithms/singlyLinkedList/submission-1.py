class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedList:
    
    def __init__(self):
        self.head=ListNode(-1)
        self.tail=self.head
    
    def get(self, index: int) -> int:
        cur = self.head.next
        i=0
        while cur:
            if i==index:
                return cur.val
            cur = cur.next
            i +=1
        return -1

    def insertHead(self, val: int) -> None:
        newnode = ListNode(val)
        newnode.next=self.head.next
        self.head.next=newnode

        if not newnode.next:
            self.tail=newnode
        
    def insertTail(self, val: int) -> None:
        self.tail.next=ListNode(val)
        self.tail=self.tail.next
        

    def remove(self, index: int) -> bool:
        i=0
        curr = self.head
        
        while i<index and curr:
            curr = curr.next
            i+=1

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail=curr
            curr.next = curr.next.next
            return True
        return False
        

    def getValues(self) -> List[int]:
        curr = self.head.next
        res=[]
        while curr :
            res.append(curr.val)
            curr = curr.next
        return res
        
