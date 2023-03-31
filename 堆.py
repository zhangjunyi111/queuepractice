import heapq
import random

L = [1, 2, 3, 5, 4, 9, 7, 6]
l2 = []
l3 = list(range(10))

# 重新打乱
random.shuffle(l3)
print(l3)
for i in l3:
    heapq.heappush(l2, i)
# heapq.heappush(l2, 3)
print(l2)

# 删除堆顶最小的元素
heapq.heappop(l2)
print(l2)
print(heapq.nlargest(1, l2))
print(heapq.nsmallest(1, l2))
