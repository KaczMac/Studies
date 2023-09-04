import time
with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()
S = ' '.join(text).lower()

def naive(s,w):
    count = 0
    t_start = time.perf_counter()
    m = 0
    i = 0
    m0 = m
    pattern = 0
    while m+len(w) < len(s)+1:
        i = 0
        temp = True
        # print(m)
        while i < len(w):
            count += 1
            if s[m+i] != w[i]:
                temp = False
                break
            else:
                i += 1
        if temp:
            pattern += 1
        m += 1
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    return count, pattern

def make_string(first, second, third = None):
    s = str(first) + "; " + str(second)
    if third:
        s += "; "+ str(third)
    return s

def hash(word):
     hw = 0
     d = 256
     q = 101
     for i in range(len(word)):
          hw = (hw*d + ord(word[i])) % q
     return hw

def rabin_karp(s,w):
    t_start = time.perf_counter()
    d = 256
    q = 101
    hw = hash(w)   
    n = len(w)
    h = 1
    for i in range(n-1):
        h = (h*d)%q
    count = 0
    pattern = 0
    colision = 0
    m = 0
    while m + n < len(s) + 1:
        count += 1
        if m==0:
            hs = hash(s[0:n])
        else:
            hs = (d*(hs - ord(s[m-1])*h) + ord(s[m-1 + n])) % q
        if hs < 0:
            hs += q
        if hs == hw:
            if s[m:m+n] == w:
                pattern += 1
            else:
                colision += 1
        m += 1
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    return count, pattern, colision


def kmp_table(w):
    pos = 1
    cnd = 0
    t = [0] * (len(w) + 1)
    t[0] = -1
    while pos < len(w):
        if w[pos] == w[cnd]:
            t[pos] = t[cnd]
        else:
            t[pos] = cnd
            while cnd >= 0 and w[pos] != w[cnd]:
                cnd = t[cnd]
        pos += 1
        cnd += 1
    t[pos] = cnd
    return t


def kmp(s,w):
    t_start = time.perf_counter()
    m = 0
    i = 0
    t = kmp_table(w)
    count = 0
    pattern = 0
    while m < len(s):
        count += 1
        if w[i] == s[m]:
            m += 1
            i += 1
            if i == len(w):
                pattern += 1
                i = 0
        else:
            i = t[i]
            if i < t[i]:
                m += 1
                i += 1
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    return count, pattern, t


a,b = naive(S, "time.")
print(make_string(a,b))
a,b,c = rabin_karp(S, "time.")
print(make_string(a,b,c))
a,b,c = kmp(S, "time.")
print(make_string(a,b,c))