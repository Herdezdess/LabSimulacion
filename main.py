import pygame
import yaml
from processing.objetos import Generador
from processing.Simulacion import DIBUJITOS

with open("configuration.yaml", "r") as f:
  config = yaml.safe_load(f)

pygame.init()
pantalla = pygame.display.set_mode((config['simulacion']['ancho'], config['simulacion']['alto']))
pygame.display.set_caption("Simulación de Gravitación")

generador = Generador(config)
obje = generador.generar_objetos()

sim = DIBUJITOS(obje, config)

running = True
while running:
  pantalla.fill((0, 0, 0))
  for obj in obje:
    obj.crear_figura(pantalla)

  sim.simular()
  pygame.display.flip()

  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False

pygame.quit()

