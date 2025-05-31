    #inputs:
    #   f: funcion para buscar la raiz
    #   a: Limite inferior del intervalo
    #   b: Limite superior del intervalo 
    #   tol: tolerancia, error maximo permitido
    #
    #outputs:
    #   raiz: valor de la raiz aproximado
    #   error: error con el que se obtuvo la solucion
def biseccion(f, a, b, tol = 0.0001, max_iter = 1000):
    count = 0
    fa = f(a)
    fb = f(b)
    #Primero comprobamos si hay solucion entre el intervalo
    #Teorema de Bolzano (valor intermedio)
    if fa*fb > 0:
        return f"No hay solucion entre [{a},{b}]"
    #Luego verificamos si la solucion es a o b
    if abs(fa) < tol:
        return a, abs(fa), count
    elif abs(fb) < tol:
        return b, abs(fb), count
    #Ahora comienza el proceso iterativo,
    #Vemos si el error es mayor al tolerado
    while (b-a)/2 > tol and count < max_iter:
        #Calculamos C y vemos si es solucion
        c = (a+b)/2
        fc = f(c)
        if abs(fc) < tol:
            return c, abs(fc), count
        #Actualizamos los valores de a,b segun corresponda
        if fc * fa < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        count += 1
    #Retornamos el valor a la solucion mas cercano
    return (a+b)/2, abs((b-a)/2), count

#Complejidad Algoritmo: 
#   Tiempo O(log((b-a)/tol)), dado que cada vez el itervalo se parte a la mitad: (b-a)/2**n <= tol
#   Espacio O(1), constante 
