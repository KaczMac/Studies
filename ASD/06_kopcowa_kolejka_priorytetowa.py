class Element:
    def __init__(self,data,priority) -> None:
        self.__data = data
        self.__priority = priority
    def __lt__(self,other):
        return self.__priority < other.__priority
    def __gt__(self,other):
        return self.__priority > other.__priority
    def __str__(self) -> str:
        return (f'{self.__priority}: {self.__data}')

class Heap:
    def __init__(self) -> None:
        self.items = []
        self.size = 0
    
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
    queue = Heap()
    lst = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    lst2 = "GRYMOTYLA"
    for i in range(len(lst)):
        elem = Element(lst2[i],lst[i])
        queue.enqueue(elem)
    queue.print_tree()
    queue.print_tab()
    first = queue.dequeue()
    print(queue.peek())
    queue.print_tab()
    print(first)
    while not queue.is_empty():
        print(queue.dequeue())
    queue.print_tab()

main()