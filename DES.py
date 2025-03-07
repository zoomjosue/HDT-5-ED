import numpy as np
import simpy
import random

#Se establece la configuracion de la simulacion
SEMILLA = 10
random.seed(SEMILLA)
MEMORIA = 100
VELOCIDAD_DE_INSTRUCCIONES = 3

#Esta funcion representa un proceso que requiere memoria y CPU para ejecutarse
#env: entorno de simulacion de SimPy
#RAM: contenedor que simula la memoria RAM disponible
#CPU: recurso que representa el procesador
#tiempo_total: lista donde se almacenan los tiempos de ejecución de los procesos
def proceso (env, RAM, CPU,tiempo_total):
    memoria = random.randint(1, 10)
    instrucciones = random.randint(1, 10)
    tiempo_inicio = env.now

    yield RAM.get(memoria)

    while instrucciones > 0:
        with CPU.request() as req:
            yield req
            yield env.timeout(1)
            instrucciones -= min(VELOCIDAD_DE_INSTRUCCIONES, instrucciones)
            
            if instrucciones == 0:
                break
            elif random.randint(1, 2) == 1:
                yield env.timeout(1)

    yield RAM.put(memoria)
    
    tiempo_total.append(env.now - tiempo_inicio)

#Esta funcion se encarga de ejecutar la simulacion de procesos en un etorno SimPy
#procesos: número total de procesos a simular
#intervalo: tiempo promedio de llegada de nuevos procesos (exponencial)
#memoria: capacidad total de la memoria RAM
#cpus: cantidad de unidades de procesamiento disponibles
#velocidad_instrucciones: cantidad de instrucciones que se procesan por unidad de tiempo
#retorna la media y la desviacion estandar de los tiempos de ejecucion
def ejecutar_simulacion(procesos, intervalo, memoria, cpus, velocidad_instrucciones):
    env = simpy.Environment()
    RAM = simpy.Container(env, init=memoria, capacity=memoria)
    CPU = simpy.Resource(env, capacity=cpus)
    tiempos = []

    def generar_procesos():
        for i in range(procesos):
            env.process(proceso(env, RAM, CPU, tiempos))
            yield env.timeout(random.expovariate(1.0/intervalo))
    
    env.process(generar_procesos())
    env.run()

    return np.mean(tiempos), np.std(tiempos)