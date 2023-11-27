"""
Trouver tout les nombres premiers inférieur a un nombre donner 
"""

def nPremier(nDonné : int) -> list:
    listPremier = []
    for nInRow in range(1,nDonné):
        listPremier.insert(0,nInRow)
        for nInOrder in range(2,nInRow-1):
            if nInRow % nInOrder == 0:
                listPremier.pop(0)
                break
    return listPremier

print(nPremier(100))

