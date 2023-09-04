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

class Sort:
    def __init__(self,lst):
        self.lst = lst
        self.size = len(lst)

    def swap(self):
        for i in range(self.size-1):
            idx = self.lst[i:].index(min(self.lst[i:])) + i
            self.lst[idx], self.lst[i] = self.lst[i], self.lst[idx]
         
    def shift(self):
        for i in range(self.size-1):
            idx = self.lst[i:].index(min(self.lst[i:])) + i
            self.lst.pop(idx)
            self.lst.insert(i,min(self.lst[i:]))
    
    def print_tab(self):
        print ('{', end=' ')
        print(*self.lst[:self.size], sep=', ', end = ' ')
        print( '}')
    

def main():




    list = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    for i in range(len(list)):
        test = [Element(list[i][1],list[i][0]) for i in range(len(list) - 1)]
    queue = Sort(test)
    queue_swap = queue
    queue_swap.swap()
    queue_swap.print_tab()
    # Metoda niestabilna
    list = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    for i in range(len(list)):
        test = [Element(list[i][1],list[i][0]) for i in range(len(list) - 1)]
    queue = Sort(test)
    queue_shift = queue

    queue_shift.shift()

    queue_shift.print_tab()
    # Metoda stabilna
    tab = []
    for i in range(10000):
        tab.append(int(random.random() * 100))
    queue2 = Sort(tab)
    t_start = time.perf_counter()
    queue_shift = queue2
    queue_shift.shift()
    queue_shift.print_tab()
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    tab = []
    for i in range(10000):
        tab.append(int(random.random() * 100))
    queue2 = Sort(tab)
    t_start = time.perf_counter()
    queue_swap = queue2
    queue_swap.swap()
    queue_swap.print_tab()
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
main()