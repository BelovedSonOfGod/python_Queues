

class Queue:
    def __init__(self):
        self.list=[]
        self._size = 0  # track length like len()
    def __len__(self):
        return self._size
    
    def __iter__(self):
        current = self.list
        for value in current:
            yield value

    def __getitem__(self,index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        for _ in range(index):
            current=self.list[_]
        return current
    
    def enqueue(self,value):
        self.list.append(value)
        self._size+=1
    def dequeue(self):
        if self._size==0:
            raise BufferError("Cannot dequeue, head is empty")
        self.list.pop(0)
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
        
    