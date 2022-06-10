import random

def idoformat(t):
    return str(t // 60) + ":" + str(t % 60).zfill(2)

def szokeres(szavak,n):
    szuro = [x for x in range(len(szavak)) if len(szavak[x]) <= n]
    if len(szuro) > 0:
        return random.randint(0,len(szuro)-1)
    else:
        return False
    
def szo_elhelyezes(szavak,n):
    racs = [[0 for x in range(n)] for j in range(n)]
    for i in szavak:
        random_koord = (random.randint(0,len(racs)-1), random.randint(0,len(racs)-1))#allista, pozicio
        szo = szokeres(szavak, n-random_koord[1])
    if szo != False:
        for j in range(n-(random_koord[1]-1), n+1):
            print(j)
            racs[random_koord[0]][j] = szavak[szo][j]
        print("OK")
    print(racs)


szo_elhelyezes(["aaa","bbb","aaaa","bbbb","aaaaa","bbbbb","aaaaaa","bbbbbb","aaaaaaa","bbbbbbb"],4)