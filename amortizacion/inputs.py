# Inputs
credito = float(input("Cuál es el monto del credito: "))
tipo_de_periodo = input('¿Qué tipo de periodos tiene el credito? (mensual, trimestral, semestral, anual): ')
periodos = float(input('¿Cuántos periodos tiene?: '))
tasa = float(input('¿De cuánto es la tasa de interés? (sin el signo de porcentage): '))/100
periodo_tasa = input('¿Qué tipo de periodos tiene la tasa? (mensual, trimestral, semestral, anual): ')
spread = float(input('¿De cuánto es el spread?: '))/100
cuota = float(input('¿De cuánto es la cuota?: '))
saldo_ant = ()
amortizacion = ()


# Tasas
def interes(tipo_de_periodo, periodos, tasa, periodo_tasa, spread):
    


# Amortizacion
def amort(amortizacion):
    pass




# Saldo incial

def sld_ini(credito, amort):
    pass


# Inversion

investment = int(input('¿Cuánto necesita tu negocio?: '))

# Info credito

percentage = int(input('¿Cuánto deseas cubrir con la linea de credito?: '))/100
credit = investment*percentage

gracia = input('¿Tienes periodo de gracia?: ')

if gracia.lower() == 'no':
    periodo_gra = 0
elif gracia.lower() == 'si':
    periodo_gra = input('¿Cuál es el periodo de gracia?: ')
    tiempo = input('Mensiona si es en meses, trimestres, semestres o años: ')

cuota = int(input('¿Cuanto es el valor de la cuota?: '))
num_cuotas = int(input('Número de cuotas: '))
periodo_cuotas = input('¿Que periodicidad tienen las cuotas?: ')

# Resumen del credito

print(credit)
print(f'El credito tiene un periodo de gracia de {periodo_gra} {tiempo}')
print(f'Con cuotas de {cuota} a {periodo_cuotas}')






