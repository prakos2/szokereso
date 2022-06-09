import random

def idoformat(t):
    return str(t // 60) + ":" + str(t % 60).zfill(2)

def szokeres(szavak,n):
    tomb=[]
    for i in range(len(szavak)):
        if len(szavak[i])<=n:
            tomb.append(szavak[i])
    for i in range(len(tomb)):
        return tomb

def szo_elhelyezes(szavak,n):
    szo_grid = [[0 for x in range(n)] for j in range(n)]
    for i in szavak:
        koordinata=(random.randint(0,n-1),random.randint(0,n-1))#allista, elem
        szo_grid[koordinata[0]][koordinata[1]]="M"
        for j in szo_grid:
            print(j)
        print(n-koordinata[1])
        if len(i)<=n-koordinata[1]:
            print("megfelel")
        else:
            print("nem felel meg")

szavak=["aaa","bbb","aaaa","bbbb","aaaaa","bbbbb","aaaaaa","bbbbbb","aaaaaaa","bbbbbbb"]
n=4
tomb=szokeres(szavak,n)
szo_elhelyezes(tomb,n)