def saralash(ro_yxat):
    yangi_ro_yxat = []
    for satr in ro_yxat:
        yangi_satr = ''.join(sorted(satr))
        yangi_ro_yxat.append(yangi_satr)
    return yangi_ro_yxat

ro_yxat = ["cba", "zyx", "nmo"]
print(saralash(ro_yxat))
