from math import inf

def string_compare(P, T, i, j):
    if i == 0:
        return j
    if j == 0:
        return i
    zamian = string_compare(P, T, i - 1, j - 1) + (P[i] != T[j])
    wstawien = string_compare(P, T, i, j - 1) + 1
    usuniec = string_compare(P, T, i - 1, j) + 1

    return min(zamian, wstawien, usuniec)


def PD(P, T):
    D = [[0 for _ in range(len(T))] for _ in range(len(P))]
    for row in range(len(P)):
        D[row][0] = row
    for col in range(len(T)):
        D[0][col] = col

    parents = [['X' for _ in range(len(T))] for _ in range(len(P))]
    for row in range(len(P)):
        parents[row][0] = 'D'
    for col in range(len(T)):
        parents[0][col] = 'I'
    parents[0][0] = 'X'

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            zamian = D[i - 1][j - 1] + (P[i] != T[j])
            wstawien = D[i][j - 1] + 1
            usuniec = D[i - 1][j] + 1

            najnizszy_koszt = min(zamian, wstawien, usuniec)
            if zamian == najnizszy_koszt:
                if P[i] == T[j]:
                    parents[i][j] = 'M'
                else:
                    parents[i][j] = 'S'
            else:
                if wstawien == najnizszy_koszt:
                    parents[i][j] = 'I'
                else:
                    parents[i][j] = 'D'

            D[i][j] = najnizszy_koszt
    return D[-1][-1], parents


def odtwarzanie_sciezki(P, T):
    parents = PD(P, T)[1]
    i = len(P) - 1
    j = len(T) - 1
    path = ''
    while i >= 0 and j >= 0:
        if parents[i][j] == 'X':
            break
        path += parents[i][j]
        if parents[i][j] == 'M' or parents[i][j] == 'S':
            i -= 1
            j -= 1
        else:
            j -= 1
    return path[::-1]


def dopasowanie_podciagow(P, T):
    D = [[0 for _ in range(len(T))] for _ in range(len(P))]
    for row in range(len(P)):
        D[row][0] = row

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            zamian = D[i - 1][j - 1] + (P[i] != T[j])
            wstawien = D[i][j - 1] + 1
            usuniec = D[i - 1][j] + 1
            D[i][j] = min(zamian, wstawien, usuniec)

    min_value = D[-1][0]
    index = 0
    for col in range(len(T)):
        if D[-1][col] < min_value:
            min_value = D[-1][col]
            index = col
    return index - len(P) + 2


def najdluzsza_wspolna_sekwencja(P, T):
    D = [[0 for _ in range(len(T))] for _ in range(len(P))]
    for row in range(len(P)):
        D[row][0] = row
    for col in range(len(T)):
        D[0][col] = col

    parents = [['X' for _ in range(len(T))] for _ in range(len(P))]
    for row in range(len(P)):
        parents[row][0] = 'D'
    for col in range(len(T)):
        parents[0][col] = 'I'
    parents[0][0] = 'X'

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            if P[i] != T[j]:
                zamian = D[i - 1][j - 1] + 999
            else:
                zamian = D[i - 1][j - 1]
            wstawien = D[i][j - 1] + 1
            usuniec = D[i - 1][j] + 1

            najnizszy_koszt = min(zamian, wstawien, usuniec)
            if zamian == najnizszy_koszt:
                if P[i] == T[j]:
                    parents[i][j] = 'M'
                else:
                    parents[i][j] = 'S'
            else:
                if wstawien == najnizszy_koszt:
                    parents[i][j] = 'I'
                else:
                    parents[i][j] = 'D'
            D[i][j] = najnizszy_koszt

    i = len(P) - 1
    j = len(T) - 1
    path = ''
    while i >= 0 and j >= 0:
        if parents[i][j] == 'X':
            break
        path += parents[i][j]
        if parents[i][j] == 'M' or parents[i][j] == 'S':
            i -= 1
            j -= 1
        elif parents[i][j] == 'D':
            i -= 1
        else:
            j -= 1

    path = path[::-1]

    index = 1
    indexes = []
    for elem in path:
        if elem != 'D':
            if elem == 'M':
                indexes.append(index)
            index += 1

    result = ''
    for i in indexes:
        result += T[i]
    return result


def najdluzsza_podsekwencja_monotoniczna(T):
    P_ = sorted(T)
    P = ''
    for elem in P_:
        P += elem

    D = [[0 for _ in range(len(T))] for _ in range(len(P))]
    for row in range(len(P)):
        D[row][0] = row
    for col in range(len(T)):
        D[0][col] = col

    parents = [['X' for _ in range(len(T))] for _ in range(len(P))]
    for row in range(len(P)):
        parents[row][0] = 'D'
    for col in range(len(T)):
        parents[0][col] = 'I'
    parents[0][0] = 'X'

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            if P[i] != T[j]:
                zamian = inf
            else:
                zamian = D[i - 1][j - 1]
            wstawien = D[i][j - 1] + 1
            usuniec = D[i - 1][j] + 1

            najnizszy_koszt = min(zamian, wstawien, usuniec)
            if zamian == najnizszy_koszt:
                if P[i] == T[j]:
                    parents[i][j] = 'M'
                else:
                    parents[i][j] = 'S'
            else:
                if wstawien == najnizszy_koszt:
                    parents[i][j] = 'I'
                else:
                    parents[i][j] = 'D'
            D[i][j] = najnizszy_koszt

    i = len(P) - 1
    j = len(T) - 1
    path = ''
    while i >= 0 and j >= 0:
        if parents[i][j] == 'X':
            break
        path += parents[i][j]
        if parents[i][j] == 'M' or parents[i][j] == 'S':
            i -= 1
            j -= 1
        elif parents[i][j] == 'D':
            i -= 1
        else:
            j -= 1

    path = path[::-1]

    index = 1
    indexes = []
    for elem in path:
        if elem != 'D':
            if elem == 'M':
                indexes.append(index)
            index += 1

    result = ''
    for i in indexes:
        result += T[i]
    return result
