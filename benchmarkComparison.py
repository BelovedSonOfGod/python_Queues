import timeit
from SimpleQueueWLinkedList import Queue as LinkedListQueue
from SimpleQueueWList import Queue as ListQueue
from collections import deque

# Setup for LinkedQueue
setup_linked = """
from __main__ import LinkedListQueue
q = LinkedListQueue()
for i in range(10000):
    q.enqueue(i)
"""

# Setup for ListQueue
setup_list = """
from __main__ import ListQueue
q = ListQueue()
for i in range(10000):
    q.enqueue(i)
"""

# Setup for deque
setup_deque = """
from collections import deque
q = deque()
for i in range(10000):
    q.append(i)
"""

print("LinkedList Dequeue:", timeit.timeit("q.dequeue()", setup=setup_linked, number=10000, globals=globals()))
print("List Dequeue:", timeit.timeit("q.dequeue()", setup=setup_list, number=10000, globals=globals()))
print("Deque popleft:", timeit.timeit("q.popleft()", setup=setup_deque, number=10000, globals=globals()))