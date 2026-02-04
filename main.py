#################################################
###[SMA - TP : Intégrales - Sommes de Riemann]###
#################################################
### Zerofish0
#################################################

## Imports
import math

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

## Définitions de fonctions
f = lambda x : (4 * np.exp(x))/(3 + np.exp(x)) # fonction étudiée

def aire_inferieure(interval_min,interval_max,n) :
    """Sommes des rectangles sous la courbe.
    parametres : 
    - interval_min : int : le début de l'intervalle sur lequel on veut estimer l'intégrale
    - interval_max : int : le maximum de cette intervalle
    - n : int : le nombre de rectangles
    return : 
    - somme_rect : int : la somme de l'aire des rectangles sous la courbe
    """
    d = abs(interval_max-interval_min)
    w = d/n

    somme_rect = int()
    for rect in range(n) :
        xi = interval_min + rect * w
        if f(xi) >= 0 : 
            hi = f(xi)
            somme_rect += w * hi
            plt.bar(xi+(w/2),hi,width = w,alpha = 0.5,color = "yellow")
        else : 
            hi = f(xi + w)
            somme_rect += w * hi
            plt.bar(xi+(w/2),hi,width = w,alpha = 0.5,color = "yellow") 
    return somme_rect

def aire_superieure(interval_min,interval_max,n) :
    """Sommes des rectangles depassant la courbe.
    parametres : 
    - interval_min : int : le début de l'intervalle sur lequel on veut estimer l'intégrale
    - interval_max : int : le maximum de cette intervalle
    - n : int : le nombre de rectangles
    return : 
    - somme_rect : int : la somme de l'aire des rectangles dépassant la courbe
    """
    d = abs(interval_max-interval_min)
    w = d/n

    somme_rect = int()
    for rect in range(n) :
        xi = interval_min + rect * w
        if f(xi) >= 0 : 
            hi = f(xi+w)
            somme_rect += w * hi
            plt.bar(xi+(w/2),hi,width = w,alpha = 0.25,color = "red")
        else : 
            hi = f(xi)
            somme_rect += w * hi
            plt.bar(xi+(w/2),hi,width = w,alpha = 0.25,color = "red") 
    return somme_rect

def valeur_approchee(interval_min,interval_max,precision) :
    """Détermine la valeur de n la plus adaptée pour avoir une précision de 'precision'.
    parametres : 
    - interval_min : int : le début de l'intervalle sur lequel on veut estimer l'intégrale
    - interval_max : int : le maximum de cette intervalle
    - precision : int : valeur à laquelle la différence entre l'estimation maximale et minimale doit être inférieure ou égale (ex. 0.01)
    return : 
    - int : l'aire approximee
    """
    n = 1
    while (aire_superieure(interval_min,interval_max,n) - aire_inferieure(interval_min,interval_max,n)) >= precision :
        n += 1
    return (aire_inferieure(interval_min,interval_max,n),aire_superieure(interval_min,interval_max,n),(aire_superieure(interval_min,interval_max,n)+aire_inferieure(interval_min,interval_max,n))/2)

## Programme principal
print("###[Intégrales - Sommes de Riemann]###")
MIN = int(input("Entrez une borne inferieure pour l'intervalle d'etude : "))
MAX = int(input("Entrez une borne superieure pour l'intervalle d'etude : "))
N = int(input("Entrez le nombre de rectangles à utliser pour l'estimation : "))

x = np.linspace(MIN, MAX, abs(MAX-MIN) * 10)
y = f(x)

inf = aire_inferieure(MIN,MAX,N)
sup = aire_superieure(MIN,MAX,N)
approx = (inf+sup)/2
plt.bar(0, 0.00000000000000000000000000000000001, width=0.00000000000000000000000000000000001, label=f'Aire inférieure : {round(inf,2)} u.a.', alpha=0.5, color='orange')
plt.bar(0, 0.00000000000000000000000000000000001, width=0.00000000000000000000000000000000001, label=f'Aire supérieure : {round(sup,2)} u.a.', alpha=0.25, color='red')
plt.bar(0, 0.00000000000000000000000000000000001, width=0.00000000000000000000000000000000001, label=f'Aire moyenne : {round(approx,2)} u.a.', alpha=0.25, color='blue')
plt.bar(0, 0.00000000000000000000000000000000001, width=0.00000000000000000000000000000000001, label=f'Nombre de rectangles : {N}', alpha=0.25)
# Tracer le graphique
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(f'Graphique de f(x) sur [{MIN};{MAX}]')
plt.grid(True)
plt.show()