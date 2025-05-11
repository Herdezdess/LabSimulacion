import numpy as np
import random
from processing.distribuciones import Distribuciones
import pygame

class Pelotas:
    def __init__(self, tipo, config):
        self.tipo = tipo
        self.config = config
        self.dist = Distribuciones(config)
        self.masa = max(1, self.dist.gaussiana(
            config['distribuciones']["media_gaussiana"],
            config['distribuciones']['gaussiana_desviacion'],
            1
        )[0])
        self.x = self.dist.uniforme(0, config['simulacion']['alto_espacio'], 1)[0]
        self.y = self.dist.uniforme(0, config['simulacion']['ancho_espacio'], 1)[0]
        self.radio = int(self.masa ** (1/2))
        self.color = np.random.rand(3)

        # Inicialización de las velocidades
        self.velocidad_x = 0  # Velocidad en el eje X
        self.velocidad_y = 0  # Velocidad en el eje Y

    def crear_figura(self, pantalla, config):
        tamaño = int(self.masa * config['simulacion']['M'])

        if self.tipo == "circulo":
            pygame.draw.circle(pantalla, self.color, (int(self.x), int(self.y)), int(self.radio))
        elif self.tipo == "cuadrado":
            pygame.draw.rect(pantalla, self.color, (int(self.x - tamaño), int(self.y - tamaño), int(2 * tamaño), int(2 * tamaño)))
        elif self.tipo == "triangulo":
            puntos = [
                (int(self.x), int(self.y + tamaño)),
                (int(self.x - tamaño), int(self.y - tamaño)),
                (int(self.x + tamaño), int(self.y - tamaño))
            ]
            pygame.draw.polygon(pantalla, self.color, puntos)


class Generador:
  def __init__(self, config):
        self.config = config
        self.dist = Distribuciones(config)

  def generar_objetos(self):
    pelotas_nuevas = []
    num_objetos = self.config['simulacion']['N']
    
    for _ in range(num_objetos):
      tipo = random.choice(["circulo", "cuadrado", "triangulo"])
      pelotas_nuevas.append(Pelotas(tipo, self.config))
    return pelotas_nuevas
