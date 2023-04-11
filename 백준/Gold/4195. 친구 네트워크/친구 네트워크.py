# 아이디어 : 
# 알고리즘 : union-find

import sys
input = sys.stdin.readline

def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b) :
    a = find(a)
    b = find(b)
    
    if a != b :
        parent[b] = a
        number[a] += number[b]
    
    print(number[a])
    
T = int(input())

for _ in range(T) :
    f = int(input())
    parent, number = dict(), dict()
    
    for _ in range(f) :
        a, b = input().split()
        
        if a not in parent :
            parent[a] = a
            number[a] = 1
        
        if b not in parent :
            parent[b] = b
            number[b] = 1
            
        union(a, b)