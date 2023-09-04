def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i<oldSize else None  for i in range(size)]

class Queue:
    def __init__(self) -> None:
        self.tab = [None for i in range(5)]
        self.size = 5
        self.idx_back = 0
        self.idx_front = 0
    
    def is_empty(self):
        return self.idx_back == self.idx_front
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[self.idx_front]
    
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            result = self.peek()
            self.idx_front += 1
            if self.idx_front == self.size:
                self.idx_front = 0
            return result
    def enqueue(self,data):
        self.tab[self.idx_back] = data
        self.idx_back = (self.idx_back + 1)%self.size
        if self.is_empty():
            self.tab = self.tab[:self.idx_back] + [None for i in range(self.size)] + self.tab[self.idx_back:]
            self.size *= 2
            self.idx_front = 0


    def __str__(self):
        if self.is_empty():
            return "[]"
        elif (self.idx_front < self.idx_back):
            return str(self.tab[self.idx_front:self.idx_back])
        else:
            return str(self.tab[self.idx_back:self.idx_front])    
        
    def print_tab(self):
        print(self.tab)

queue = Queue()
dane = [1,2,3,4]
for i in dane:
    queue.enqueue(i)
print(queue.dequeue())
peek = queue.peek()
print(peek)
print(queue)
drugie_dane = [5,6,7,8]
for i in drugie_dane:
    queue.enqueue(i)
queue.print_tab()
for i in range(queue.size):
    j = queue.dequeue()
    print(j)
print(queue)

# class Queue:
#     def __init__(self):
#         self.tab = [None for i in range(5)]
#         self.size = 5
#         self.id_in = 0
#         self.id_out = 0
        
#     def is_empty(self):
#         if self.id_in == self.id_out:
#             return True
#         else:
#             return False
        
#     def peek(self):
#         if self.is_empty():
#             return None
#         else:
#             return self.tab[self.id_out]
         
#     def dequeue(self):
#         if self.is_empty():
#             return None
#         else:
#             temp = self.id_out
#             self.id_out = (self.id_out + 1) % self.size
#             return self.tab[temp]    

#     def enqueue(self, data):
#         self.tab[self.id_in] = data
#         self.id_in = (self.id_in + 1) % self.size
#         if self.id_in == self.id_out:
#             self.tab = self.tab[:self.id_out] + [None for i in range(self.size)] + self.tab[self.id_out:]
#             self.size *= 2
#             self.id_out = 0

#     def __str__(self):
#         if self.is_empty():
#             return "[]"
#         elif (self.id_in < self.id_out):
#             return str(self.tab[self.id_in:self.id_out])
#         else:
#             return str(self.tab[self.id_out:self.id_in])            

#     def print_tab(self):
#         print(self.tab)


# queue = Queue()
# dane1 = [1,2,3,4]
# for i in dane1:
#     queue.enqueue(i)

# first = queue.dequeue()
# print('Pierwsza wpisana dana: ',first)

# sec = queue.peek()
# print('Druga wpisana dana: ',sec)

# print(queue) 

# dane2 = [5,6,7,8]
# for i in dane2:
#     queue.enqueue(i)

# queue.print_tab()

# while not queue.is_empty():
#     data = queue.dequeue()
#     print(data)

# print(queue)