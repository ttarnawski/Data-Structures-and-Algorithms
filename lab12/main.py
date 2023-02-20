from lab12 import naiv_method
from lab12 import kmp_search
from lab12 import rabin_karp
import time

with open('lotr.txt', encoding='utf-8') as f:
    text = f.readlines()

S = ''.join(text).lower()

t_start = time.perf_counter()
print(naiv_method(S, 'time.'))
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

t_start = time.perf_counter()
print(rabin_karp(S, 'time.'))
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

t_start = time.perf_counter()
print(kmp_search(S, 'time.'))
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
