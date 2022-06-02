from random import randint

def szavak_elhelyezese(random_szavak_szama,szavak_max_merete):
    szavak=[]
    #fajlbeolvasas és fajlrendezes
    with open("C:\\Users\\Komlósi Ádám\\Desktop\\szokereso\\assets\\szavak.txt",'r',encoding='utf-8-sig') as fajl:
        for i in fajl:
            szavak.append(i.split(';'))
    #random szo generalas es szavak max merete
    random_szavak=[]
    ciklus=True
    for i in range(random_szavak_szama):
        while ciklus==True:
                random_szo_szama=randint(0,len(szavak[0]))
                if len(szavak[0][random_szo_szama])<=szavak_max_merete:
                    random_szavak.append(szavak[0][random_szo_szama])
                    ciklus=False
                else:
                    ciklus=True
        ciklus=True
    print(random_szavak)
    #leghosszab szo meretu oszlopok es sorok
    leghosszabb_szo=0
    for i in range(len(random_szavak)):
        if len(random_szavak[i])>leghosszabb_szo:
            leghosszabb_szo=len(random_szavak[i])
    n=leghosszabb_szo
    #paratlan szamu oszlopok es sorok kizarasa
    if n>6:
        n=8
    if n==5:
        n=6
    if n==3:
        n=4
    #paros szamu sorok es oszlopok
    if n%2==0:
        #sorok es oszlopok letrehozasa (n*n)
        tomb=[]
        for i in range(n):
            tomb.append([])#sorok
            for j in range(n):
                tomb[i].append(0)#oszlopok
    print(tomb)
szavak_elhelyezese(5,8)#szavak szama, szavak max hossza