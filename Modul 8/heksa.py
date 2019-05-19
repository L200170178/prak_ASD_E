class Stack(object):
    def __init__(self):
        self.items =[]
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.items)
    def peek(self):
        assert not self.isEmpty()
        return self.items[-1]
    def pop(self):
        assert not self.isEmpty()
        return self.items.pop()
    def push(self,data):
        self.items.append(data)

def cetakHeksa(d):
    f = Stack()
    hexalist ='0123456789ABCDEF'
    while d !=0:
        sisa = d%16
        d = d//16
        f.push(hexalist[sisa])
    st = ''
    for i in range(len(f)):
        st = st + str(f.pop())
    return st


###############################nomor 2 ############################

nilai = Stack()
for i in range(16):
    if i % 3 == 0:
        nilai.push(i)
        print(nilai.items)

##############################nomor 3 #############################
        
nilai = Stack()
for i in range(16):
    if i % 3 == 0:
        nilai.push(i)
    elif i % 4 == 0:
        nilai.pop()
print(nilai.items)
