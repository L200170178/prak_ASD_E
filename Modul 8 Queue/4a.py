class Queue():
    def __init__(self):
        self.qlist = []
    def is_empty(self):
        return len(self) == 0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self, data):
        self.qlist.append(data)
    def dequeue(self):
        assert not self.is_empty(), 'Antrian sedang kosoong'
        return self.qlist.pop(0)
    def getFrontMost(self):
        assert not self.is_empty(), 'Antrian sedang kosoong'
        return self.qlist[0]
    def getRearMost(self):
        assert not self.is_empty(), 'Antrian sedang kosoong'
        return self.qlist[-1]

q = Queue()
q.enqueue(15)
q.enqueue(20)
q.enqueue(25)
q.enqueue(30)
q.enqueue(35)

print(q.getFrontMost())
print(q.getRearMost())
print(q.qlist)
