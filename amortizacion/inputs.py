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
    if matfin == '1':
        presente = float(input("¿Cuánto quieres invertir?: "))
        periodos = input('¿Por cuanto tiempo quieres dejar la inversión?: ')
        valores = periodos.split()
        if len(valores) == 2:
            n = float(valores[0])
        tasa = input('¿De cuánto es la tasa de interés? (sin el signo de porcentage): ')
        interes = tasa.split()
        if len(interes) == 2:
            i = float(interes[0])/100 
        valor = presente*((1+i)**n)
        analisis = f'Si inviertes {presente} a {periodos}, con una tasa de {tasa} el valor futuro de tu inversión será: {valor}'
        # analisis = f'El valor futuro de tu inversión de {presente} por {peridos} '
    elif matfin == '2':
        futuro = float(input("¿Cuánto quieres tener acumulado en tu inversión?: "))
        periodos = input('¿Por cuanto tiempo quieres dejar la inversión?: ')
        valores = periodos.split() 
        if len(valores) == 2:
            n = float(valores[0])
        tasa = input('¿De cuánto es la tasa de interés? (sin el signo de porcentage): ')
        interes = tasa.split()
        if len(interes) == 2:
            i = float(interes[0])/100
        valor = futuro/((1+i)**n)
        analisis = f'Si quieres tener {futuro} en {periodos}, con una tasa de {tasa}, hoy tienes que invertir: {valor}'
    else:
        analisis = 'Prueba otra vez'
    return analisis

print("")
print(escenario())

