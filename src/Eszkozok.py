import random
def bemenetellenor(elem, tipus):
    '''
    Ellenőrzi egy elem típusát, ha nem biztonságos megfelelővé teszi azt
    '''
    if type(elem) == tipus:
        return elem
    else:
        #print(f"[F] [Eszkozok] Megadott elem típusa nem megfelelő. ({str(type(elem))}) ({str(tipus)})")
        try:
            uj_elem = tipus(elem) # Megpróbálkozás típuskényszerítéssel
            print(f"[I] [Eszkozok] Típuskényszerítés ({str(type(elem))}) => ({str(tipus)})")
        except:
            uj_elem = str(elem)     # Ha sikertelen, egy üres típus visszaadása
        return uj_elem

def idoformat(t):
    return str(t // 60) + ":" + str(t % 60).zfill(2)