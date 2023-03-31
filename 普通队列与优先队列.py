from queue import  Queue

from queue import PriorityQueue

q = Queue(3)
q.put("3")
q.put("2")
q.put("1")
# while q.not_empty:#   x = q.get()
 #   print(x)


q2 = PriorityQueue()
q2.put("3")
q2.put("2")
q2.put("1")
while q2.not_empty:
    x = q2.get()
    print(x)
exit()