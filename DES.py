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