import pandas as pd
from tabulate import tabulate


n = [1, 2, 3, 4, 5]
saldo_inicial = [2000, 1000, 500, 250, 100]
interes = [12, 12, 12, 12, 12]
cuotas = [300, 300, 300, 300, 300]
amortizacion = [421, 421, 421, 421, 421]
saldo_final = [1800, 800, 400, 150, 0]


table = {
    'Periodo': n,
    'Saldo inicial': saldo_inicial,
    'Intereses': interes,
    'Cuota': cuotas,
    'Amortizacion': amortizacion,
    'Saldo final': saldo_final
}

print(tabulate(table, headers="keys", tablefmt="fancy_grid"))