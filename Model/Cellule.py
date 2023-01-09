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

def construireCellule(val:int=0,visible:bool=False,annotation:str=None)->dict:
    if type(visible)!=bool:
        raise TypeError(f"construireCellule : le second paramètre {type(visible)} n’est pas un booléen")
    if val != const.ID_MINE:
        if (val < 0 or val > 8):
            raise ValueError(f"construireCellule : le contenu {val} n’est pas correct ")
    dictio={const.CONTENU:val,const.VISIBLE:visible,const.ANNOTATION:annotation}
    return dictio

def getContenuCellule(d:dict)->int:
    if type_cellule(d)==False:
        raise TypeError("getContenuCellule : Le paramètre n’est pas une cellule")
    return d[const.CONTENU]

def isVisibleCellule(d:dict)->bool:
    if type_cellule(d) == False:
        raise TypeError("isVisibleCellule : Le paramètre n’est pas une cellule.")
    return d[const.VISIBLE]

def setContenuCellule(d:dict,val:int)->None:
    if type(val)!=int:
        raise TypeError("setContenuCellule : Le second paramètre n’est pas un entier")
    if val != const.ID_MINE:
        if (val < 0 or val > 8):
            raise ValueError(f"setContenuCellule : la valeur du contenu {val} n’est pas correcte")
    if type_cellule(d)==False:
        raise TypeError("setContenuCellule : Le premier paramètre n’est pas une cellule.")

    d[const.CONTENU] = val
    return None

def setVisibleCellule(d:dict,visi:bool)->None:
    if type_cellule(d) == False:
        raise TypeError("setVisibleCellule : Le premier paramètre n’est pas une cellule.")
    if type(visi)!=bool:
        raise TypeError("setVisibleCellule : Le second paramètre n’est pas un booléen")
    d[const.VISIBLE]=visi
    return None

def contientMineCellule(d:dict)->bool:
    if type_cellule(d)==False:
        raise TypeError("contientMineCellule : Le paramètre n’est pas une cellule")
    return d[const.CONTENU]==const.ID_MINE

def isAnnotationCorrecte(annotation:str)->bool:
    val=[None,const.DOUTE,const.FLAG]
    res=False
    if annotation in val :
        res=True
    return res

def getAnnotationCellule(d:dict)->str:
    if type_cellule(d)==False:
        raise TypeError(f"getAnnotationCellule : le paramètre {d} n’est pas une cellule")
    return d.get(const.ANNOTATION,None)

def changeAnnotationCellule(d:dict)->None:
    if type_cellule(d)==False:
        raise TypeError("changeAnnotationCellule : le paramètre n’est pas une cellule ")
    val=[None,const.FLAG,const.DOUTE]
    #si l'index est égal à 2-> on retourne à l'index 0
    i=val.index(getAnnotationCellule(d))
    if i==2:
        i=0
        d[const.ANNOTATION]=val[i]
    else:
        i+=1
        d[const.ANNOTATION] = val[i]
    return None
