import numpy as np
# from sklearn.tree import DecisionTreeClassifier
from tabulate import tabulate
# import pandas

import inputs
import tables

# Inputs
credito = float(input("Cuál es el monto del credito: "))
tipo_de_periodo = input('¿Qué tipo de periodos tiene el credito? (mensual, trimestral, semestral, anual): ')
periodos = float(input('¿Cuántos periodos tiene?: '))
tasa = float(input('¿De cuánto es la tasa de interés? (sin el signo de porcentage): '))/100
periodo_tasa = input('¿Qué tipo de periodos tiene la tasa? (mensual, trimestral, semestral, anual): ')
spread = float(input('¿De cuánto es el spread?: '))/100
cuota = float(input('¿De cuánto es la cuota?: '))
saldo_ant = ()
amort = ()
