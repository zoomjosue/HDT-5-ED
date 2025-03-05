from DES import ejecutar_simulacion, MEMORIA, VELOCIDAD_DE_INSTRUCCIONES

INTERVALOS = [10, 5, 1]
NUM_PROCESOS = [25, 50, 100, 150, 200]

if __name__ == "__main__":
    for intervalo in INTERVALOS:
        for num_procesos in NUM_PROCESOS:
            tiempo_medio, desviacion = ejecutar_simulacion(
                num_procesos, intervalo, MEMORIA, 1, VELOCIDAD_DE_INSTRUCCIONES
            )
            print(f'Intervalo: {intervalo}, Procesos: {num_procesos}, Tiempo promedio: {tiempo_medio:.2f}, Desviacion: {desviacion:.2f}')
