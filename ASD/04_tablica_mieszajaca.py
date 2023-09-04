class Element:
    def __init__(self,key,value) -> None:
        self.key = key
        self.value = value

class HashTable:
    def __init__(self,size,c1 = 1, c2 = 0) -> None:
        self.tab = [None for i in range(size)]
        self.c1 = c1
        self.c2 = c2
        self.size = size

    def mix(self, key):
        value = key
        if isinstance(key, str):
            value = 0
            for i in key:
                value += ord(i)
        return value % self.size
    
    def open_adress(self,index,attempt):
        return (index + (self.c1 * attempt) + (self.c2 * attempt**2)) % self.size
    
    def search(self, key):
        index = self.mix(key)
        if (self.tab[index] is None):
            return
        else:
            if (self.tab[index].key is not None) and (self.tab[index].key == key):
                return self.tab[index].value
            else:
                for i in range(1,self.size + 1):
                    new_index = self.open_adress(index,i)
                    if (self.tab[new_index].key is not None) and (self.tab[new_index].key == key):
                        return self.tab[new_index].value

        
    def insert(self, key, value):
        index = self.mix(key)
        if (self.tab[index] is None) or (self.tab[index].key == key) or (self.tab[index].key is None):
            self.tab[index] = Element(key,value)
        else:
            for i in range(1,self.size + 1):
                new_index = self.open_adress(index,i)
                if (self.tab[new_index] is None) or (self.tab[new_index].key == key) or (self.tab[new_index].key is None):
                    break
                else:
                    new_index = None
            if new_index is None:
                raise MemoryError
            else:
                self.tab[new_index] = Element(key,value)

    def remove(self, key):
        index = self.mix(key)
        removed = None
        if (self.tab[index] is None):
            return None
        else:
            if (self.tab[index].key is not None) and (self.tab[index].key == key):
                removed = index
            else:
                for i in (1,self.size + 1):
                    new_index = self.open_adress(index,i)
                    if (self.tab[new_index].key is not None) and (self.tab[new_index].key == key):
                        break
                removed = new_index
        if removed is not None:
            self.tab[removed] = None
    
    def __str__(self) -> str:
        elems = '['
        for i in range(self.size):
            if self.tab[i] is None:
                elems += 'None, '
            else:
                elems += '{' + str(self.tab[i].key) + ':' + str(self.tab[i].value) + '}, '
        elems += ']'
        elems = elems.replace(', ]',']')
        return str(elems)

def error_insert(tab,key,value):
    try:
        tab.insert(key, value)
    except MemoryError:
        print("Brak miejsca")

def fun1(key,val,c1=1,c2=0):
    tab = HashTable(13,c1,c2)
    for i in range(15):
        error_insert(tab,key[i],val[i])
    print(tab)
    print(tab.search(5))
    print(tab.search(14))
    error_insert(tab,5,'Z')
    print(tab.search(5))
    tab.remove(5)
    print(tab)
    print(tab.search(31))
    error_insert(tab,"test","W")
    print(tab)

keys = [1,2,3,4,5,18,31,8,9,10,11,12,13,14,15]
values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
fun1(keys,values)

def fun2(val,c1 = 1,c2 = 0):
    tab = HashTable(13,c1,c2)
    for i in range(13):
        error_insert(tab,13 + 13*i,val[i])
    print(tab)

fun2(values)
fun2(values,0,1)
fun1(keys,values,0,1)