def punto_fijo(f, x0, tol = 0.0001, max_iter = 1000):   
    count = 0
    error = float('inf')

    while error > tol and count < max_iter:
        x1 = f(x0)
        error = abs(x1-x0)
        x0 = x1
        count += 1
    
    convergencia = error <= tol
    return x0, error, count, convergencia

