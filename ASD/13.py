import numpy as np
def string_compare_rec(P,T,i,j):
    if i == 0:
        return j
    if j == 0:
        return i
    zamian = string_compare_rec(P,T,i-1,j-1) + (P[i]!=T[j])
    wstawien = string_compare_rec(P,T,i,j-1) +1
    usuniec = string_compare_rec(P,T,i-1,j) + 1
    return min(zamian,wstawien,usuniec)

def string_compare_pd(P,T,i,j):

    lenT = len(T)
    lenP = len(P)
    D = [[0 for k in range(lenT)]for l in range(lenP)]
    parent = [["X" for k in range(lenT)]for l in range(lenP)]
    for k in range(lenP):
        D[k][0] = k
    for l in range(lenT):
        D[0][l] = l
    for l in range(1,len(parent[0])):
        parent[0][l] = "I"
    for k in range(1,len(parent)):
        parent[k][0] = "D"

    for k in range(1,i+1):
        for l in range(1,j+1):
            zamian = D[k-1][l-1] + (P[k]!=T[l])
            wstawien = D[k][l-1] +1
            usuniec = D[k-1][l] + 1
            minimal = min(zamian,wstawien,usuniec)
            D[k][l] = minimal
            if minimal == zamian:
                if P[k] == T[l]:
                    parent[k][l] = "M"
                else:
                    parent[k][l] = "S"
            elif minimal == wstawien:
                parent[k][l] = "I"
            else:
                parent[k][l] = "D"

    parent[0][0] = "X"
    path = get_path(parent)
    return D[lenP - 1][lenT - 1], path

def get_path(parent):
    i = len(parent) - 1
    j = len(parent[0]) - 1
    s = ""
    temp = parent[i][j]
    while temp != "X":
        s += temp
        # print(i,j)
        # print(temp)
        if (temp == "M") or (temp == "S"):
            i -= 1
            j -= 1
        elif temp == "D":
            i -= 1
        elif temp == "I":
            j -= 1
        temp = parent[i][j]
    return s[::-1]

def string_compare_pd2(P,T,i,j):
    lenT = len(T)
    lenP = len(P)
    D = [[0 for k in range(lenT)]for l in range(lenP)]
    parent = [["X" for k in range(lenT)]for l in range(lenP)]
    for k in range(lenP):
        D[k][0] = k
    # for l in range(lenT):
    #     D[0][l] = l
    # for l in range(1,len(parent[0])):
    #     parent[0][l] = "I"
    for k in range(1,len(parent)):
        parent[k][0] = "D"

    for k in range(1,i+1):
        for l in range(1,j+1):
            zamian = D[k-1][l-1] + (P[k]!=T[l])
            wstawien = D[k][l-1] +1
            usuniec = D[k-1][l] + 1
            minimal = min(zamian,wstawien,usuniec)
            D[k][l] = minimal
            if minimal == zamian:
                if P[k] == T[l]:
                    parent[k][l] = "M"
                else:
                    parent[k][l] = "S"
            elif minimal == wstawien:
                parent[k][l] = "I"
            else:
                parent[k][l] = "D"

    k = len(P) - 1
    l = 0
    for m in range(lenT):
        if D[k][m] < D[k][l]:
            l = m
    return l - lenP + 2

def string_compare_pd3(P,T,i,j):
    lenT = len(T)
    lenP = len(P)
    D = [[0 for k in range(lenT)]for l in range(lenP)]
    parent = [["X" for k in range(lenT)]for l in range(lenP)]
    for k in range(lenP):
        D[k][0] = k
    for l in range(lenT):
        D[0][l] = l
    for l in range(1,len(parent[0])):
        parent[0][l] = "I"
    for k in range(1,len(parent)):
        parent[k][0] = "D"

    for k in range(1,i+1):
        for l in range(1,j+1):
            if P[k]!=T[l]:
                zamian = D[k-1][l-1] + 10000000
            else:
                zamian = D[k-1][l-1]
            wstawien = D[k][l-1] +1
            usuniec = D[k-1][l] + 1
            minimal = min(zamian,wstawien,usuniec)
            D[k][l] = minimal
            if minimal == zamian:
                if P[k] == T[l]:
                    parent[k][l] = "M"
                else:
                    parent[k][l] = "S"
            elif minimal == wstawien:
                parent[k][l] = "I"
            else:
                parent[k][l] = "D"
    parent[0][0] = "X"
    path = get_path(parent)
    sequence = longest_sequence(parent,P)
    return D[lenP - 1][lenT - 1], path, sequence

def longest_sequence(parent, P):
    i = len(parent) - 1
    j = len(parent[0]) - 1
    s = ""
    temp = parent[i][j]

    while temp != "X":
        if temp == "D":
            i -= 1
        elif temp == "I":
            j -= 1
        else:
            i -= 1
            j -= 1
        if temp == "M":
            s += P[i+1]
        temp = parent[i][j]
    return s[::-1]
def main():
    print(string_compare_rec(" kot"," pies",len(" kot")-1,len(" pies")-1))
    P = ' biały autobus'
    T = ' czarny autokar'
    mat, path = string_compare_pd(P,T,len(P)-1,len(T)-1)
    print(mat)
    P = ' thou shalt not'
    T = ' you should not'
    print(string_compare_pd(P,T,len(P)-1,len(T)-1))

    P = ' ban'
    T = ' mokeyssbanana'
    idx = string_compare_pd2(P,T,len(P)-1,len(T)-1)
    print(idx)
    P = ' bin'
    T = ' mokeyssbanana'
    idx = string_compare_pd2(P,T,len(P)-1,len(T)-1)
    print(idx)
    P = ' democrat'
    T = ' republican'
    d,path,seq = string_compare_pd3(P,T,len(P)-1,len(T)-1)
    print(seq)
    T = ' 243517698'
    P = ''.join(sorted(T))
    d,path,seq = string_compare_pd3(P,T,len(P)-1,len(T)-1)
    print(seq)
    
main()