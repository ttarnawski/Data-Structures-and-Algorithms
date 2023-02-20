#!/usr/bin/python
# -*- coding: utf-8 -*-

class LinkedList:
    def __init__(self):
        self.head = None

    def destroy(self):
        self.head = None

    def add(self, node):
        node.next = self.head
        self.head = node

    def remove(self):
        self.head = self.head.next

    def is_empty(self):
        return True if self.head is None else False

    def length(self):
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        return length

    def get(self):
        return self.head

    def add_on_last(self, data):
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = data

    def remove_from_last(self):
        node = self.head
        while node.next.next is not None:
            node = node.next
        node.next = None

    @staticmethod
    def take(n, data):
        new_list = LinkedList()
        if n >= 1:
            if n > len(data):
                n = len(data)
            new_list.head = Node(data[0])
            node = new_list.head
            for i in range(n - 1):
                node.next = Node(data[i + 1])
                node = node.next
        return new_list

    @staticmethod
    def drop(n, data):
        new_list = LinkedList()
        if n >= 1:
            if n >= len(data):
                return new_list
            new_list.head = Node(data[n])
            node = new_list.head
            for i in range(n + 1, len(data)):
                node.next = Node(data[i])
                node = node.next
        return new_list

    def __str__(self):
        nodes_list = []
        node = self.head
        while node is not None:
            nodes_list.append(node)
            node = node.next
        string = ', '.join(map(str, nodes_list))
        return string


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
