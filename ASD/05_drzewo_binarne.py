class Child:
    def __init__(self,key,value) -> None:
        self.key = key
        self.value = value
        self.lchild = None
        self.rchild = None
        

class Tree:
    def __init__(self) -> None:
        self.root = None
    
    def search_fun(self,node: Child,key):
        if node is None:
            return None
        elif node.key == key:
            return node
        elif node.key > key:
            return self.search_fun(node.lchild,key)
        elif node.key < key:
            return self.search_fun(node.rchild,key)
        
    def search(self,key):
        sought = self.search_fun(self.root,key)
        if sought.key == key:
            return sought.value
        elif sought is None:
            return None

    def insert_fun(self,node: Child,key,value):
        if node is None:
            return Child(key,value)
        elif node.key > key:
            node.lchild = self.insert_fun(node.lchild,key,value)
            return node
        elif node.key < key:
            node.rchild = self.insert_fun(node.rchild,key,value)
            return node
        else:
            node.value = value
            return node
        
    def insert(self,key,value):
        if self.root is None:
            self.root = Child(key,value)
        else:
            self.insert_fun(self.root,key,value)

    def delete(self, node: Child, key):
        if node is None:
            return None
        elif key < node.key:
            node.lchild = self.delete(node.lchild, key)
        elif key > node.key:
            node.rchild = self.delete(node.rchild, key)
        else:
            if node.lchild is None:
                temp = node.rchild
                node = None
                return temp
            elif node.rchild is None:
                temp = node.lchild
                node = None
                return temp
            else:
                temp = self.find_min_node(node.rchild)
                node.key = temp.key
                node.value = temp.value
                node.rchild = self.delete(node.rchild, temp.key)
        return node

    def find_min_node(self, node):
        current = node
        while current.lchild is not None:
            current = current.lchild
        return current

    def height(self,node: Child):
        if node is None:
            return -1
        
        left_height = self.height(node.lchild)
        right_height = self.height(node.rchild)
        
        return max(left_height, right_height) + 1
    
    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.rchild, lvl+5)

            print()
            print(lvl*" ", node.key, node.value)
     
            self.__print_tree(node.lchild, lvl+5)
    
    def get_all(self):
        nodes_list = []
        self.__get_all(self.root, nodes_list)
        return nodes_list

    def __get_all(self, node: Child, nodes_list: list):
        if node is not None:
            self.__get_all(node.lchild, nodes_list)
            nodes_list.append(node)
            self.__get_all(node.rchild, nodes_list)
    def print(self):
        nodes_list = self.get_all()
        for i in nodes_list:
            print(f'{i.key} {i.value},', end= " ")
        


def main():
    tree = Tree()
    tree.insert(50,'A')
    tree.insert(15,'B')
    tree.insert(62,'C')
    tree.insert(5,'D')
    tree.insert(20,'E')
    tree.insert(58,'F')
    tree.insert(91,'G')
    tree.insert(3,'H')
    tree.insert(8,'I')
    tree.insert(37,'J')
    tree.insert(60,'K')
    tree.insert(24,'L')

    tree.print_tree()
    tree.print()

    node = tree.search(24)
    print("\n")
    print(f"Wartość dla klucza 24: {node}")
    tree.insert(20, 'AA')
    tree.insert(6,'M')
    tree.delete(tree.root, 62)
    tree.insert(59,'N')
    tree.insert(100,'P')
    tree.delete(tree.root, 8)
    tree.delete(tree.root, 15)
    tree.insert(55,'R')
    tree.delete(tree.root, 50)
    tree.delete(tree.root, 5)
    tree.delete(tree.root, 24)
    print("\n")
    print("Wysokość drzewa:", tree.height(tree.root))

    tree.print()
    print("\n")
    tree.print_tree()

main()