import numpy as np
import simpy
import random

SEMILLA = 10
random.seed(SEMILLA)
MEMORIA = 100
VELOCIDAD_DE_INSTRUCCIONES = 3
PROCESOS = [25, 50, 100, 150, 200]
INTERVALOS_DE_LLEGADA = [10, 5, 1]

def proceso (env, RAM, CPU):
    memoria = random.randint(1, 10)
    instrucciones = random.randint(1, 10)
    tiempo_inicio = env.now

    yield RAM.get(memoria)

    while instrucciones > 0:
        with CPU.request() as req:
            yield req
            yield env.timeout(1)
            instrucciones -= VELOCIDAD_DE_INSTRUCCIONES

            if instrucciones == 0:
                break
            elif random.randint(1, 21) == 1:
                yield env.timeout(1)

    yield RAM.put(memoria)
    
    tiempo_total = env.now - tiempo_inicio
    return tiempo_total

def ejecutar_simulacion(procesos, intervalo, memoria, cpus, velocidadkuchao):
    env = simpy.Environment()
    RAM = simpy.Container(env, init=memoria, capacity=memoria)
    CPU = simpy.Resource(env, capacity=cpus)
    tiempos = []

    def generar_procesos():
        for i in range(procesos):
            tiempos.append(env.process(proceso(env, RAM, CPU, velocidadkuchao, i+1)))
            yield env.timeout(random.expovariate(1.0/intervalo))
    
    env.process(generar_procesos())
    env.run()

    tiempos_finales = [env.now - t.value for t in tiempos]
    return np.mean(tiempos_finales), np.std(tiempos_finales)