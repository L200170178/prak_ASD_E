import heapq
class PriorityQueue(object):
    def __init__(self):
        self.qlist = []
    def __len__(self):
        return len(self.qlist)
    def isEmpty(self):
        return len(self) == 0
    def enqueue(self,data,priority):
        heapq.heappush(self.qlist, (priority,data))
        self.qlist.sort()
    def dequeue(self):
        return self.qlist.pop

p = PriorityQueue()

p.enqueue('123', 9)
p.enqueue('456' , 0)
p.enqueue('789', 3)

print(p.qlist)
p.dequeue()
print(p.qlist)
