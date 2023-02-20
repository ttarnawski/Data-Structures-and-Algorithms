class HeapSort:
    def __init__(self, tab=[]):
        self.tab = tab
        self.heap_size = len(tab)

    @staticmethod
    def left(index):
        return 2 * index + 1

    @staticmethod
    def right(index):
        return 2 * index + 2

    @staticmethod
    def parent(index):
        return index // 2

    def heapify(self):
        parents = []
        for i in range(len(self.tab)):
            if self.left(i) < len(self.tab):
                parents.append(i)
            else:
                break
        parents.reverse()

        for index in parents:
            while self.left(index) < len(self.tab) and self.right(index) < len(self.tab):
                if self.tab[index] < self.tab[self.left(index)] or self.tab[index] < self.tab[self.right(index)]:
                    if self.tab[self.left(index)] > self.tab[self.right(index)]:
                        self.tab[self.left(index)], self.tab[index] = self.tab[index], self.tab[self.left(index)]
                        index = self.left(index)
                    else:
                        self.tab[self.right(index)], self.tab[index] = self.tab[index], self.tab[self.right(index)]
                        index = self.right(index)
                else:
                    break
            while self.left(index) < len(self.tab) <= self.right(index):
                if self.tab[index] < self.tab[self.left(index)]:
                    self.tab[self.left(index)], self.tab[index] = self.tab[index], self.tab[self.left(index)]
                    index = self.left(index)
                else:
                    break

    def heap_sort(self):
        for i in range(self.heap_size):
            index = 0
            self.tab[index], self.tab[self.heap_size - 1] = self.tab[self.heap_size - 1], self.tab[index]
            self.heap_size -= 1
            while self.left(index) < self.heap_size and self.right(index) < self.heap_size:
                if self.tab[index] < self.tab[self.left(index)] or self.tab[index] < self.tab[self.right(index)]:
                    if self.tab[self.left(index)] > self.tab[self.right(index)]:
                        self.tab[self.left(index)], self.tab[index] = self.tab[index], self.tab[self.left(index)]
                        index = self.left(index)
                    else:
                        self.tab[self.right(index)], self.tab[index] = self.tab[index], self.tab[self.right(index)]
                        index = self.right(index)
                else:
                    break
            while self.left(index) < self.heap_size <= self.right(index):
                if self.tab[index] < self.tab[self.left(index)]:
                    self.tab[self.left(index)], self.tab[index] = self.tab[index], self.tab[self.left(index)]
                    index = self.left(index)
                else:
                    break

    def enqueue(self, priority, data=None):
        if not self.tab:
            self.tab.append(Node(priority, data))
            self.heap_size += 1
        else:
            index = len(self.tab)
            node = Node(priority, data)
            self.tab.append(node)
            self.heap_size += 1
            while node > self.tab[self.parent(index)]:
                self.tab[index], self.tab[self.parent(index)] = self.tab[self.parent(index)], self.tab[index]
                index = self.parent(index)

    def print_tab(self):
        print('{', end=' ')
        for i in range(len(self.tab) - 1):
            print(self.tab[i], end=', ')
        if len(self.tab) != 0: print(self.tab[-1], end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < len(self.tab):
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)


class Node:
    def __init__(self, priority, data):
        self.priority = priority
        self.data = data

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __repr__(self):
        return str(self.priority) + ' : ' + str(self.data)


def selection_sort_swap(tab):
    for i in range(len(tab)):
        index = i
        for j in range(i + 1, len(tab)):
            if tab[j] < tab[index]:
                index = j
        tab[i], tab[index] = tab[index], tab[i]
    return tab

def selection_sort_shift(tab):
    for i in range(len(tab)):
        index = i
        for j in range(i, len(tab)):
            if tab[j] < tab[index]:
                index = j
        tab.insert(index, tab.pop(i))
        tab.insert(i, tab.pop(index - 1))
    return tab



