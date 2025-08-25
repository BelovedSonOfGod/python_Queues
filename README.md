# Queues implementation in Python  

This repository contains  **Two different Python approaches**, where I implemented a **single queue with linked list** with objects and **one with list** list from python.  

The purpose of this project is to practice:  
- Python classes and objects.  
- Pointers/references (`Next` node).  
- Basic operations on queues.  

---

## Features  
The linked list supports the following operations:  
- `Enqueue`: Adds an element to the end (tail) of the queue.
- `Dequeue`: Removes the element from the front of the queue. If the queue is empty, an underflow error occurs.
- `Peek/Front`: Returns the element at the front without removing it.
- `Size`: Returns the number of elements in the queue.
- `isEmpty`: Returns true if the queue is empty, otherwise false. 

---

## Example Usage  
```python
from linked_list import LinkedList

# Create a new linked list
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

# Output example: 10 -> 20
# 30 -> 40 -> 50
# 40 -> 50

```

## Benchmark
Using timeinit, initialize the collections (also comparing with collections from python library) to meaure up time.
