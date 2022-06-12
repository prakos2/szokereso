import random

def bemenetellenor(elem, tipus):
    '''
    Ellenőrzi egy elem típusát, ha nem biztonságos megfelelővé teszi azt
    '''
    if type(elem) == tipus:
        return elem
    else:
        try:
            uj_elem = tipus(elem) # Megpróbálkozás típuskényszerítéssel
        except:
            uj_elem = str(elem)     # Ha sikertelen, egy str típus visszaadása
        return uj_elem

def idoformat(t):
    return str(t // 60) + ":" + str(t % 60).zfill(2)