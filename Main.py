#Autores:
#- José Manuel Sanchez Hernández - 24092
#- Josué Antonio Isaac García Barrera - 24918
#- José Alberto Abril Suchite - 24585

#Se ejecuta multiples simulaciones variando la cantidad de procesos, el intervalo de llegada, la 
#memoria disponible y la cantidad de CPUs. Se utiliza el modulo DES para realizar las simulaciones.

from DES import ejecutar_simulacion, MEMORIA, VELOCIDAD_DE_INSTRUCCIONES

#Se definenn los parametrosde la simulacion
INTERVALOS = [10, 5, 1]
NUM_PROCESOS = [25, 50, 100, 150, 200]

#Esta funcion se encarga de ejecutar simulaciones con diferentes configuraciones y almacena los resultados.
#memoria: capacidad total de la memoria RAM
#cpus: cantidad de unidades de procesamiento disponibles
#velocidad_instrucciones: cantidad de instrucciones que se procesan por unidad de tiempo
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

#Se ejecutan  diferentes configuraciones de simulación para analizar cual es mas viable
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