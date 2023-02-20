#!/usr/bin/python
# -*- coding: utf-8 -*-

class BST:
    def __init__(self):
        self.head = None

    def search(self, key):
        return self._search(self.head, key)

    def _search(self, node, key):
        if self.head is None:
            return None
        else:
            if key < node.key:
                if node.left is None:
                    return None
                else:
                    return self._search(node.left, key)
            elif key > node.key:
                if node.right is None:
                    return None
                else:
                    return self._search(node.right, key)
            else:
                return node.value

    def insert(self, key, value):
        self._insert(self.head, key, value)

    def _insert(self, node, key, value):
        if node is None:
            self.head = BSTNode(key, value)
        else:
            if key < node.key:
                if node.left is None:
                    node.left = BSTNode(key, value)
                else:
                    node.left = self._insert(node.left, key, value)
                return node
            elif key > node.key:
                if node.right is None:
                    node.right = BSTNode(key, value)
                else:
                    node.right = self._insert(node.right, key, value)
                return node
            else:
                node.value = value
                return node

    def delete(self, key):
        self._delete(self.head, key)

    def _delete(self, node, key):
        if node is None:
            return None
        else:
            if key < node.key:
                node.left = self._delete(node.left, key)
            elif key > node.key:
                node.right = self._delete(node.right, key)
            else:
                if node.left is None:
                    pointer_node = node.right
                    node = None
                    return pointer_node
                elif node.right is None:
                    pointer_node = node.left
                    node = None
                    return pointer_node

                current_node = node.right
                while current_node.left is not None:
                    current_node = current_node.left
                pointer_node = current_node
                node.key = pointer_node.key
                node.value = pointer_node.value
                node.right = self._delete(node.right, pointer_node.key)
            return node

    def height(self, starting_node):
        if starting_node is None:
            return 0
        else:
            left_height = self.height(starting_node.left)
            right_height = self.height(starting_node.right)
            return max(left_height, right_height) + 1

    def print(self):
        tab = self._print(self.head, tab=[])
        for node in tab:
            print('{0}:{1}'.format(node[0], node[1]), end=' ')
        print()

    def _print(self, node, tab):
        if node is None:
            return None
        else:
            self._print(node.left, tab)
            tab.append((node.key, node.value))
            self._print(node.right, tab)
        return tab

    def print_tree(self):
        print("==============")
        self._print_tree(self.head, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node is not None:
            self._print_tree(node.right, lvl + 5)
            print()
            print(lvl * " ", node.key, node.value)
            self._print_tree(node.left, lvl + 5)


class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
