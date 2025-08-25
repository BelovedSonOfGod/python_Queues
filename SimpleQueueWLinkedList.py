
class Node:
    def __init__(self,value,next:id):
        self.value=value
        self.next=next
 

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
        self._size = 0  # track length like len()
    def __len__(self):
        return self._size
    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next
    def __getitem__(self,index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value
    
    def enqueue(self,value):
        newNodeToAddToTail= Node(value,None)

        if self.tail==None:
            self.head=newNodeToAddToTail
            self.tail=newNodeToAddToTail
        else:
            self.tail.next=newNodeToAddToTail
            self.tail=newNodeToAddToTail
        self._size+=1
    def dequeue(self):
        if self.head==None:
            raise BufferError("Cannot dequeue, head is empty")
        if self.head==self.tail:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
        self._size-=1


    def peek(self):
        return self[0]
    
    def size(self):
        return len(self)
    def isEmpty(self):
        if(len(self)==0):
            return True
        else:
            return False

    def __str__(self):
        return " -> ".join(str(x) for x in self)
    
if __name__=="__main__":
    q= Queue()
    q.enqueue(10)
    q.enqueue(20)
    print(q)

    q.dequeue()
    q.dequeue()

    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    print(q)
    q.dequeue()
    print(q)
        
    