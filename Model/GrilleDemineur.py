# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                            and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True

def construireGrilleDemineur(nl:int,nc:int)->list:
    if type(nl)!=int or type(nc)!=int:
        raise TypeError(f"« construireGrilleDemineur : Le nombre de lignes {type(nl)} ou de colonnes {type(nc)} n’est pas un entier.")
    if nl<=0 or nc<=0:
        raise ValueError(f"construireGrilleDemineur : Le nombre de lignes {nl} ou de colonnes {nc}) est négatif ou nul")
    res=[]
    for i in range(nl):
        tmp=[]
        for j in range(nc):
            tmp.append(construireCellule())
        res.append(tmp)
    return res

def getNbLignesGrilleDemineur(grille:list)->int:
    if type_grille_demineur(grille)==False:
        raise TypeError("getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(grille)

def getNbColonnesGrilleDemineur(grille:list)->int:
    if type_grille_demineur(grille) == False:
        raise TypeError(" getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(grille[0])

def isCoordonneeCorrecte(grille:list,coord:tuple)->bool:
    if type_grille_demineur(grille)==False or type(coord)!=tuple:
        raise TypeError("isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")
    res=False
    (i,j)=coord
    if i>=0 :
        if i<getNbLignesGrilleDemineur(grille):
            if j>=0:
                if j<getNbColonnesGrilleDemineur(grille):
                    res=True
    return res

def getCelluleGrilleDemineur(grille:list,coord:tuple)->dict:
    if type_grille_demineur(grille)==False or type(coord)!=tuple:
        raise TypeError("getCelluleGrilleDemineur : un des paramètres n’est pas du bon type.")
    if isCoordonneeCorrecte(grille,coord)==False:
        raise IndexError("getCelluleGrilleDemineur : coordonnée non contenue dans la grille")
    return grille[coord[0]][coord[1]]

def getContenuGrilleDemineur(grille:list,coord:tuple)->int:
    return getCelluleGrilleDemineur(grille,coord)[const.CONTENU]

def  setContenuGrilleDemineur(grille:list,coord:tuple,val:int)->None:
    if type(val)!=int:
        raise TypeError("setContenuGrilleDemineur: le 3ème paramètre n'est pas un entier ")
    if val!=const.ID_MINE:
        if val<0 or val>8:
            raise ValueError(f"setContenuGrilleDemineur: le contenu {val} n'est pas correct ")
    getCelluleGrilleDemineur(grille,coord)[const.CONTENU]=val
    return None

def isVisibleGrilleDemineur(grille:list,coord:tuple)->bool:
    return getCelluleGrilleDemineur(grille,coord)[const.VISIBLE]

def setVisibleGrilleDemineur(grille:list,coord:tuple,visi:bool)->None:
    if type(visi)!=bool:
        raise TypeError("setVisibleGrilleDemineur: ")
    getCelluleGrilleDemineur(grille,coord)[const.VISIBLE]=visi
    return None

def contientMineGrilleDemineur(grille:list,coord:tuple)->bool:
    return getCelluleGrilleDemineur(grille,coord)[const.CONTENU]==const.ID_MINE

def getCoordonneeVoisinsGrilleDemineur(grille:list,coord:tuple)->list:
    if type_grille_demineur(grille)==False or type(coord)!=tuple:
        raise TypeError("getCoordonneeVoisinsGrilleDemineur : un des paramètres n’est pas du bon type")
    if isCoordonneeCorrecte(grille,coord)==False:
        raise IndexError(" getCoordonneeVoisinsGrilleDemineur : la coordonnée n’est pas dans la grille")
    res=[]
    for i in range(coord[0]-1,coord[0]+2):
        for j in range(coord[1]-1,coord[1]+2):
            if isCoordonneeCorrecte(grille,(i,j))==True and (i,j)!=coord:
                res.append((i,j))
    return res

def placerMinesGrilleDemineur(grille:list,nb:int,coord:tuple)->None:
    if nb<=0 or (getNbLignesGrilleDemineur(grille)*(getNbColonnesGrilleDemineur(grille)))==nb:
        raise ValueError(" placerMinesGrilleDemineur : Nombre de bombes à placer incorrect")
    if isCoordonneeCorrecte(grille, coord) == False:
        raise IndexError("placerMinesGrilleDemineur : la coordonnée n’est pas dans la grille")
    lst=[]
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            if (i,j)!=coord:
                lst.append((i,j))
    shuffle(lst)
    for i in range(nb):
        setContenuGrilleDemineur(grille,lst[i],const.ID_MINE)
    compterMinesVoisinesGrilleDemineur(grille)
    return None

def compterMinesVoisinesGrilleDemineur(grille:list)->None:
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            if contientMineGrilleDemineur(grille,(i,j))==False:
                lst=getCoordonneeVoisinsGrilleDemineur(grille,(i,j))
                nb=0
                for coord in lst:
                    if contientMineGrilleDemineur(grille,coord)==True:
                        nb+=1
                setContenuGrilleDemineur(grille,(i,j),nb)
    return None


def getNbMinesGrilleDemineur(grille: list) -> int:
    if type_grille_demineur(grille) == False:
        raise ValueError("getNbMinesGrilleDemineur : le paramètre n’est pas une grille")
    nb=0
    i=0
    j=0
    ligne=getNbLignesGrilleDemineur(grille)
    colonne=getNbColonnesGrilleDemineur(grille)
    while i < ligne:
        while j<colonne:
            if contientMineGrilleDemineur(grille,(i,j))==True:
                nb+=1
            j+=1
        j=0
        i+=1
    return nb

def getAnnotationGrilleDemineur(grille:list,coord:tuple)->None:
    return getCelluleGrilleDemineur(grille,coord)[const.ANNOTATION]

def getMinesRestantesGrilleDemineur(grille: list) -> int:
    nb=getNbMinesGrilleDemineur(grille)
    i=0
    j=0
    ligne=getNbLignesGrilleDemineur(grille)
    colonne=getNbColonnesGrilleDemineur(grille)
    while i <ligne :
        while j < colonne:
            if getAnnotationGrilleDemineur(grille, (i, j)) == const.FLAG:
                nb -= 1
            j += 1
        j = 0
        i += 1
    return nb



def gagneGrilleDemineur(grille:list)->bool:
    res = True
    i = 0
    j = 0
    ligne=getNbLignesGrilleDemineur(grille)
    colonne=getNbColonnesGrilleDemineur(grille)
    while i <ligne and res==True:
        while j < colonne:
            if contientMineGrilleDemineur(grille, (i, j)) == True :
                if isVisibleGrilleDemineur(grille, (i, j)) == True:
                    if getAnnotationGrilleDemineur(grille,(i,j))==const.FLAG:
                        res = False
            else:
                if isVisibleGrilleDemineur(grille,(i,j))==False:
                    res=False
            j += 1
        j = 0
        i += 1
    return res

def perduGrilleDemineur(grille:list)->bool:
    res=False
    i=0
    j=0
    ligne=getNbLignesGrilleDemineur(grille)
    colonne=getNbColonnesGrilleDemineur(grille)
    while i<ligne and  res==False:
        while j<colonne :
            if contientMineGrilleDemineur(grille,(i,j))==True:
                if isVisibleGrilleDemineur(grille,(i,j))==True:
                    res=True
            j+=1
        j = 0
        i+=1
    return res

def reinitialiserGrilleDemineur(grille:list)->None:
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            reinitialiserCellule(grille[i][j])
    return None

def decouvrirGrilleDemineur(grille:list,coord:tuple)->set:
    lst=getCoordonneeVoisinsGrilleDemineur(grille,coord)
    res=set()
    res.add(coord)
    while len(lst)>0:
        for i in lst:
            if i not in res:
                if contientMineGrilleDemineur(grille,i)==False:
                    res.add(i)
                    lst.remove(i)
                    if getContenuGrilleDemineur(grille,i)==0:
                        lst.extend(getCoordonneeVoisinsGrilleDemineur(grille,i))
                else:
                    lst.remove(i)
            else:
                lst.remove(i)
    return res