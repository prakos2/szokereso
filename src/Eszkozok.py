import random

def idoformat(t):
    return str(t // 60) + ":" + str(t % 60).zfill(2)

def szokeres(szavak,n):
    tomb=[]
    for i in szavak:
        if len(i)<=n:
            tomb.append(i)
    return (random.randint(0,len(tomb)-1))