from DES import ejecutar_simulacion, MEMORIA, VELOCIDAD_DE_INSTRUCCIONES

INTERVALOS = [10, 5, 1]
NUM_PROCESOS = [25, 50, 100, 150, 200]

def ejecutar_experimentos(memoria, cpus, velocidad):
    resultados = []

    for intervalo in INTERVALOS:
        for num_procesos in NUM_PROCESOS:
            tiempo_medio, desviacion = ejecutar_simulacion(
                num_procesos, intervalo, memoria, cpus, velocidad
            )
            print(f'Intervalo: {intervalo}, Procesos: {num_procesos}, Tiempo promedio: {tiempo_medio:.2f}, Desviacion: {desviacion:.2f}')
            resultados.append((intervalo, num_procesos, tiempo_medio, desviacion))
        
    return resultados

if __name__ == "__main__":
    print("Simulacion con 100 de memoria y 1 CPU: \n")
    resultadoskucaho1 = ejecutar_experimentos(100, 1, VELOCIDAD_DE_INSTRUCCIONES)
    print("\n")

    print("Simulacion con 200 de memoria y 1 CPU: \n")
    resultadoskucaho2 = ejecutar_experimentos(200, 1, VELOCIDAD_DE_INSTRUCCIONES)
    print("\n")

    print("Simulacion con 100 de memoria y 1 CPU con velocidad 6: \n")
    resultadoskuchao3 = ejecutar_experimentos(100, 1, 6)
    print("\n")

    print("Simulacion con 100 de memoria y 2 CPU: \n")
    resultadoskuchao4 = ejecutar_experimentos(100, 2, VELOCIDAD_DE_INSTRUCCIONES)
    print("\n")