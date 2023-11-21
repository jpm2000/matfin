import pandas as pd
import numpy as np
from tabulate import tabulate
import inputs

def investment():
    period = np.arange(0, inputs.n)
    interest = np.array(inputs.i)
    sald_ini = np.array(inputs.presente, o*inputs.n)
    retiros = np.array(0)
    sald_fin = np.array(0*inputs.n, inputs.futuro)
    tabla = {
        'Mes': period,
        'i': interest,
        'Deposito': sald_ini,
        'Retiros': retiros,
        'Saldo final': sald_fin
    }
    return tabulate(tabla, headers='keys', tablefmt='fancy_grid')


def amort_table():
    n = np.arange(0, inputs.periodos)
    saldo_inicial = np.arange(0, inputs.periodos)
    interes = np.arange(0, inputs.periodos)
    cuotas = np.arange(0, inputs.periodos)
    amort = np.arange(0, inputs.periodos)
    saldo_final = np.arange(0, inputs.periodos)
    table = {
        'Periodo': n,
        'Saldo inicial': saldo_inicial,
        'Intereses': interes,
        'Cuota': cuotas,
        'Amortizacion': amort,
        'Saldo final': saldo_final
    }
    return tabulate(table, headers='keys', tablefmt='fancy_grid')

#print(tabulate(table, headers="keys", tablefmt="fancy_grid"))

# print(amort_table())
print('')
print(inputs)
print(investment)