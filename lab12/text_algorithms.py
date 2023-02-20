def naiv_method(S, W):
    starting_index = 0
    comparisons = 0
    result = 0

    while starting_index < (len(S)):
        m = starting_index
        i = 0
        while i < len(W):
            comparisons += 1
            if W[i] == S[m]:
                if i + 1 == len(W):
                    result += 1
                    starting_index += 1
                    break
                else:
                    i += 1
                    m += 1
            else:
                starting_index += 1
                break
    return result, comparisons


def rabin_karp(S, W):
    d = 256
    q = 101
    hW = hash(W)
    M = len(S)
    N = len(W)
    h = 1
    for i in range(N - 1):
        h = (h * d) % q
    result = 0
    comparisons = 0
    same_hash = 0

    hS = hash(S[0:N])
    for m in range(M - N):
        if hS < 0:
            hS += q
        comparisons += 1
        if hS == hW:
            if S[m:m + N] == W:
                result += 1
            else:
                same_hash += 1
        hS = (d * (hS - ord(S[m]) * h) + ord(S[m + N])) % q

    hS = hash(S[M - N:M])
    if hS < 0:
        hS += q
    comparisons += 1
    if hS == hW:
        if S[M - N:M] == W:
            result += 1
        else:
            same_hash += 1
    return result, comparisons, same_hash


def hash(word):
    d = 256
    q = 101
    hw = 0
    for i in range(len(word)):
        hw = (hw * d + ord(word[i])) % q
    return hw


def kmp_search(S, W):
    m = 0
    i = 0
    T = kmp_table(W)
    P = []
    nP = 0
    comparisons = 0

    while m < len(S):
        comparisons += 1
        if W[i] == S[m]:
            m += 1
            i += 1
            if i == len(W):
                P.append(m - 1)
                nP += 1
                i = T[i]
        else:
            i = T[i]
            if i < 0:
                m += 1
                i += 1
    return nP, comparisons


def kmp_table(W):
    pos = 1
    cnd = 0
    T = [0 for _ in range(len(W) + 1)]
    T[0] = -1

    while pos < len(W):
        if W[pos] == W[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1
    T[pos] = cnd
    return T
