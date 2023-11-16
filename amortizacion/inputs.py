# Inputs
presente = ()
futuro = ()
tipo_de_periodo = ()
periodos = ()
tasa = ()
periodo_tasa = ()
spread = ()
cuota = ()
saldo_ant = ()
amortizacion = ()


def escenario():
    print('Los modelos financiero disponibles son:')
    print('1. Valor futuro')
    print('2. Valor presete')
    matfin = input('Cual es el modelo de matematica financiero que quieres que calcule: ') 
    if matfin == '1. Valor futuro':
        presente = float(input("¿Cuánto quieres invertir?: "))
        periodos = float(input('¿Por cuanto tiempo quieres dejar la inversión?: '))
        valores = periodos.split()
        if len(valores) == 2:
            n = valores[0]
            periodicidad = valores[1]
        tasa = float(input('¿De cuánto es la tasa de interés? (sin el signo de porcentage): '))/100
        periodo_tasa = input('¿Qué tipo de periodos tiene la tasa? (mensual, trimestral, semestral, anual): ')
        valor = presente*((1+tasa)**n)
        analisis = f'El valor futuro de tu inversión de {presente} por {peridos} '
    elif matfin == '2. Valor presete':
        futuro = float(input("¿Cuánto quieres tener acumulado en tu inversión?: "))
        periodos = float(input('¿Por cuanto tiempo quieres dejar la inversión?: '))
        tasa = float(input('¿De cuánto es la tasa de interés? (sin el signo de porcentage): '))/100
        periodo_tasa = input('¿Qué tipo de periodos tiene la tasa? (mensual, trimestral, semestral, anual): ')
        valor = futuro/((1+tasa)**periodos)
    else:
        valor = 'Prueba otra vez'
    return valor


print(escenario())


'''


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
'''





