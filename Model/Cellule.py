# Model/Cellule.py
#

from Model.Constantes import *

#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)


def isContenuCorrect(val:int)->bool:
    res=True
    if type(val)==int:
        if val!=const.ID_MINE:
            if (val<0 or  val>8) :
                res=False
    else:
        res=False
    return res

def construireCellule(val:int=0,visi:bool=False)->dict:
    if type(visi)!=bool:
        raise TypeError(f"construireCellule : le second paramètre {type(visi)} n’est pas un booléen")
    if val != const.ID_MINE:
        if (val < 0 or val > 8):
            raise ValueError(f"construireCellule : le contenu {val} n’est pas correct ")
    dictio={const.CONTENU:val,const.VISIBLE:visi}
    return dictio

def getContenuCellule(d:dict)->int:
    if type_cellule(d)!=True:
        raise TypeError("getContenuCellule : Le paramètre n’est pas une cellule")
    return d[const.CONTENU]

def isVisibleCellule(d:dict)->bool:
    if type_cellule(d) == False:
        raise TypeError("isVisibleCellule : Le paramètre n’est pas une cellule.")
    return d[const.VISIBLE]

def setContenuCellule(d:dict,val:int)->None:
    if val != const.ID_MINE:
        if (val < 0 or val > 8):
            raise ValueError(f"setContenuCellule : la valeur du contenu {val} n’est pas correcte")
    d[const.CONTENU] = val
    return None
