#!/usr/bin/python
# -*- coding: utf-8 -*-

class HashTable:
    def __init__(self, size, c1=1, c2=0):
        self.size = size
        self.c1 = c1
        self.c2 = c2
        self.tab = [None for i in range(size)]

    def hash_function(self, key):
        if isinstance(key, str):
            ord_sum = 0
            for letter in key:
                ord_sum += ord(letter)
            return ord_sum % self.size
        else:
            return key % self.size

    def remove_collision(self, key):
        it = 1
        key_hash = self.hash_function(key)
        index = key_hash
        while self.tab[index] is not None:
            index = (key_hash + self.c1 * it + self.c2 * it ** 2) % self.size
            it += 1
            if it >= self.size:
              break
        return index

    def search(self, key):
        for i in range(self.size):
            if self.tab[i] is not None:
                if self.tab[i].key == key:
                    return self.tab[i].value

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.tab[index] is not None and self.tab[index].key != key:
            index = self.remove_collision(key)
            if self.tab[index] is not None:
                print('Brak miejsca')
            else:
                self.tab[index] = Element(key, value)
        else:
            self.tab[index] = Element(key, value)

    def remove(self, key):
        for i in range(self.size):
            if self.tab[i] is not None:
                if self.tab[i].key == key:
                    self.tab[i] = None

    def __str__(self):
        string = ''
        for i in range(self.size):
            if self.tab[i] is not None:
                string += '{' + str(self.tab[i].key) + ': ' + str(self.tab[i].value) + '} '
            else:
                string += 'None '
        return string


class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return '{' + str(self.key) + ': ' + str(self.value) + '}'
