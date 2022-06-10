import random

def idoformat(t):
    return str(t // 60) + ":" + str(t % 60).zfill(2)

def szokeres(szavak,n):
<<<<<<< HEAD
    tomb=[]
    for i in range(len(szavak)):
        if len(szavak[i])<=n:
            tomb.append(szavak[i])
    return tomb[random.randint(0,len(tomb)-1)]

=======
    szuro = [x for x in range(len(szavak)) if len(szavak[x]) <= n]
    if len(szuro) > 0:
        return random.randint(0,len(szuro)-1)
    else:
        return False
    
>>>>>>> c349b7548440b9ba008318c62a760446894ef668
def szo_elhelyezes(szavak,n):
    racs = [[0 for x in range(n)] for j in range(n)]
    for i in szavak:
<<<<<<< HEAD
        koordinata=(random.randint(0,n-1),random.randint(0,n-1)) # allista, elem
        for j in szo_grid:
            print(j)
        print(n-koordinata[1])
        if len(i)<=n-koordinata[1]:
            for i in range(n-koordinata[1], len(i)-1):
                szo_grid[i] = szavak[i]
        else:
            print("nem felel meg")
=======
        random_koord = (random.randint(0,len(racs)-1), random.randint(0,len(racs)-1))#allista, pozicio
        szo = szokeres(szavak, n-random_koord[1])
    if szo != False:
        for j in range(n-(random_koord[1]-1), n+1):
            print(j)
            racs[random_koord[0]][j] = szavak[szo][j]
        print("OK")
    print(racs)
>>>>>>> c349b7548440b9ba008318c62a760446894ef668


szo_elhelyezes(["aaa","bbb","aaaa","bbbb","aaaaa","bbbbb","aaaaaa","bbbbbb","aaaaaaa","bbbbbbb"],4)