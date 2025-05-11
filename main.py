import pygame
import random  # Importamos random
import config
from processing.objeto import Particula  # Importamos la clase Particula
from processing.distribuciones import generar_posicion_uniforme
from processing.simulacion import aplicar_gravedad, fusionar  # Importamos las funciones de simulación

# Inicializar Pygame
pygame.init()
pantalla = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("Simulación Gravitacional")
clock = pygame.time.Clock()

# Generar partículas usando distribuciones
particulas = []
for _ in range(config.NUM_PARTICULAS):
    x, y = generar_posicion_uniforme(config.WIDTH, config.HEIGHT)
    # Generar masa dentro del rango definido en config.py
    masa = random.uniform(config.MASA_MIN, config.MASA_MAX)
    particulas.append(Particula(x, y, masa))  # Crear partículas con la clase Particula

# Bucle principal
running = True
while running:
    clock.tick(60)
    pantalla.fill((0, 0, 0))

    # Simulación
    aplicar_gravedad(particulas)  # Aplicamos la gravedad
    for p in particulas:
        p.actualizar_pos()
        p.dibujar(pantalla)

    particulas = fusionar(particulas)  # Fusionamos las partículas cercanas

    # Evento de salida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
