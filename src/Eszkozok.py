import random

def idoformat(t):
    return str(t // 60) + ":" + str(t % 60).zfill(2)

def szokeres(szavak,n):
    tomb=[]
    for i in szavak:
        if i<=n:
            tomb.append(i)
    return tomb[random.randint(0,len(tomb))]

szavak=["aaa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa"]
szokeres(szavak,4)