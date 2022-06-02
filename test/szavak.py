from random import randint
def szavak_elhelyezese(n):
    if n%2==0:
        szavak=[]
        #fajlbeolvasas
        with open("C:\\Users\\diak\\Desktop\\szokereso\\assets\\szavak.txt",'r',encoding='utf-8') as fajl:
            for i in fajl:
                szavak.append(i)
        #sorok es oszlopok letrehozasa (n*n)
        tomb=[]
        for i in range(n):
            tomb.append([])#sorok
            for j in range(n):
                tomb[i].append(0)#oszlopok
        #szavak elhelyezkedése random sorrendben
        szo=[]
        random=randint(len(szavak))
        szo.append(szo[random])
        print(szo)
        print(tomb)

szavak_elhelyezese(4)