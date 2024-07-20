import numpy as np
from tabulate import tabulate

periodos = int(input('escribe los periodos: '))
presente = int(input('valor presente: '))
interes = presente*(int(input('tasa de interes: '))/100)
cuota = int(input("valor de la cuota: "))

n = np.arange(0, periodos)
saldo_ini = np.linspace(0,0, periodos)
saldo_ini[0] = presente
inte = np.linspace(0,0, periodos)
inte[:] = interes
pago = np.linspace(0,0, periodos)
pago[:] = cuota
saldo_final = np.arange(0, periodos)

tabla = {
    'Meses': n,
    'Saldo inicial': presente,
    'Interes': inte,
    'Cuota': pago,
    'Saldo final': saldo_final
}
print(n)
print(saldo_ini)
print(inte)
print(pago) 
print(saldo_final)

tabulate(tabla, headers='keys', tablefmt='fancy_grid')