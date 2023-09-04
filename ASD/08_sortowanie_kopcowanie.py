import random
import time
class Element:
    def __init__(self,data,priority) -> None:
        self.__data = data
        self.__priority = priority
    def __lt__(self,other):
        return self.__priority < other.__priority
    def __gt__(self,other):
        return self.__priority > other.__priority
    def __repr__(self) -> str:
        return (f'{self.__priority}: {self.__data}')

class Heap:
    def __init__(self,lst = None) -> None:
        if not lst:
            self.items = lst
            self.size = 0
        else:
            self.items = lst
            self.size = len(lst)
            for i in range(self.size-1,-1,-1):
                self.fix_up(i)
    
    def left(self, idx):
        return 2*idx + 1
    
    def right(self,idx):
        return 2*idx + 2
    
    def parent(self,idx):
        return (idx-1)//2

    def is_empty(self):
        return self.size == 0
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.items[0]
    
    
    def fix_down(self, idx):
        while True:
            lchild = self.left(idx)
            rchild = self.right(idx)

            temp = idx
            if rchild < self.size and self.items[rchild] > self.items[temp]:
                temp = rchild
            if lchild < self.size and self.items[lchild] > self.items[temp]:
                temp = lchild



            if temp != idx:
                self.items[temp], self.items[idx] = self.items[idx], self.items[temp]
                idx = temp
            else:
                return

    def dequeue(self):
        if self.is_empty():
            return None
        max_prio = self.items[0]
        self.size -= 1
        self.items[self.size], self.items[0] = self.items[0], self.items[self.size]

        self.fix_down(0)
        return max_prio

    def fix_up(self,idx):
        parent = self.parent(idx)
        while idx > 0 and self.items[idx] > self.items[parent]:
            self.items[idx], self.items[parent] = self.items[parent], self.items[idx]
            idx = parent
            parent = self.parent(idx)


    def enqueue(self,elem: Element):
        if self.size == len(self.items):
            self.items.append(elem)
        else:
            self.items[self.size] = elem
        self.size += 1
        self.fix_up(self.size-1)

    def print_tab(self):
        print ('{', end=' ')
        print(*self.items[:self.size], sep=', ', end = ' ')
        print( '}')

    def print_tree(self, idx =0 , lvl=0):
        if idx<self.size:           
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.items[idx] if self.items[idx] else None)           
            self.print_tree(self.left(idx), lvl+1)


def main():

    list = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    for i in range(len(list)):
        test = [Element(list[i][1],list[i][0]) for i in range(len(list) - 1)]
    queue = Heap(test)
    queue.print_tree()
    queue.print_tab()
    for i in queue.items:
        queue.dequeue()

    print(test)
    tab = []
    for i in range(10000):
        tab.append(int(random.random() * 100))
    
    queue2 = Heap(tab)
    # queue2.print_tree()
    t_start = time.perf_counter()
    for ii in queue2.items:
        queue2.dequeue()
    # print(tab)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
main()