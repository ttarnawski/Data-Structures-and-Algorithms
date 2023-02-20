#!/usr/bin/python
# -*- coding: utf-8 -*-

class Queue:
    def __init__(self):
        self.queue = [None for i in range(5)]
        self.size = 5
        self.read_index = 0
        self.save_index = 0

    def realloc(self, size):
        old_size = len(self.queue)
        return [self.queue[i] if i < old_size else None for i in range(size)]

    def is_empty(self):
        return self.read_index == self.save_index

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.queue[self.read_index]

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            self.read_index += 1
            if self.read_index >= len(self.queue):
                self.read_index = 0
                val, self.queue[-1] = self.queue[-1], None
                return val
            else:
                val, self.queue[self.read_index - 1] = self.queue[self.read_index - 1], None
                return val

    def enqueue(self, data):
        if self.save_index >= len(self.queue):
            self.save_index = 0
        self.queue[self.save_index] = data
        self.save_index += 1
        if self.save_index == self.read_index:
            self.queue = self.realloc(2 * self.size)
            for i in range(self.read_index, self.size):
                self.queue[i + self.size], self.queue[i] = self.queue[i], None
            self.read_index += self.size
            self.size = self.size * 2

    # wypisanie tablicy
    def array_to_str(self):
        return str(self.queue)

    # wypisanie kolejki
    def queue_to_str(self):
        return str([i for i in self.queue if i is not None])
