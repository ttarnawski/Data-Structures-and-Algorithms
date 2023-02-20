#!/usr/bin/python
# -*- coding: utf-8 -*-

class PriorityQueue:
    def __init__(self):
        self.tab = []

    def is_empty(self):
        if not self.tab:
            return True
        else:
            return False

    def peek(self):
        return self.tab[0].data

    @staticmethod
    def left(index):
        return 2 * index + 1

    @staticmethod
    def right(index):
        return 2 * index + 2

    @staticmethod
    def parent(index):
        return index // 2

    def dequeue(self):
        if not self.tab:
            return None
        elif len(self.tab) == 1:
            return self.tab.pop().data
        else:
            self.tab[0], self.tab[-1] = self.tab[-1], self.tab[0]
            pop_value = self.tab.pop()
            index = 0
            if index < len(self.tab) - 1:
                if self.right(index) < len(self.tab) - 2:
                    while self.tab[index] < self.tab[self.left(index)] or self.tab[index] < self.tab[self.right(index)]:
                        if self.tab[self.right(index)] < self.tab[self.left(index)]:
                            self.tab[index], self.tab[self.left(index)] = self.tab[self.left(index)], self.tab[index]
                            index = self.left(index)
                            if self.left(index) > len(self.tab) - 1:
                                break
                        else:
                            self.tab[index], self.tab[self.right(index)] = self.tab[self.right(index)], self.tab[index]
                            index = self.right(index)
                            if self.right(index) > len(self.tab) - 2:
                                break
                else:
                    if self.tab[index] < self.tab[self.left(index)]:
                        self.tab[index], self.tab[self.left(index)] = self.tab[self.left(index)], self.tab[index]
            return pop_value.data

    def enqueue(self, priority, data):
        if not self.tab:
            self.tab.append(Node(priority, data))
        else:
            index = len(self.tab)
            node = Node(priority, data)
            self.tab.append(node)
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

    def __str__(self):
        return str(self.priority) + ' : ' + str(self.data)
