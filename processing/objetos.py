#objetos.py
import numpy as np
import random
from processing.distribuciones import Distribuciones
import pygame

class Pelotas:
  def __init__(self, tipo, config):
    self.tipo = tipo
    self.config = config
    self.dist = Distribuciones(config)
    self.masa =  max(1, self.dist.gaussiana(
        config['distribuciones']["media_gaussiana"],
        config['distribuciones']['gaussiana_desviacion'],
        1
    )[0])
    self.x = self.dist.uniforme(0, config['simulacion']['alto_espacio'], 1)[0]
    self.y = self.dist.uniforme(0, config['simulacion']['ancho_espacio'], 1)[0]
    self.radio = int(self.masa ** (1/2))
    self.color = np.random.rand(3)

  def crear_figura(self, pantalla, config):
    tamaño = self.masa * config['simulacion']['M'] #M es la proporcion entre la masa y el tamaño del objeto

    if self.tipo == "circulo":
      pygame.draw.circle(pantalla, self.color, (int(self.x), int(self.y)), self.radio)
    elif self.tipo == "cuadrado":
      pygame.draw.rect(pantalla, self.color, (self.x - tamaño, self.y - tamaño), 2 * tamaño, 2 * tamaño)
    elif self.tipo == "triangulo":
      puntos = [
          (self.x, self.y + tamaño),
          (self.x - tamaño, self.y - tamaño),
          (self.x + tamaño, self.y - tamaño)
      ]
      pygame.draw.polygon(pantalla, self.color, puntos)

class Generador:
  def __init__(self, config):
        self.config = config
        self.dist = Distribuciones(config)

  def generar_objetos(self):
    pelotas_nuevas = []
    num_objetos = self.config['simulacion']['N']
    media_gaussiana = self.config['distribuciones']['media_gaussiana']
    gaussiana_desviacion = self.config['distribuciones']['gaussiana_desviacion']
    uniforme_min = self.config['distribuciones']['uniforme_min']
    uniforme_max = self.config['distribuciones']['uniforme_max']

    for _ in range(num_objetos):
      tipo = random.choice(["circulo", "cuadrado", "triangulo"])
      masa = self.dist.gaussiana(media_gaussiana, gaussiana_desviacion, num_objetos)
      x = self.dist.uniforme(uniforme_min, uniforme_max, num_objetos)
      y = self.dist.uniforme(uniforme_min, uniforme_max, num_objetos)
      color = np.random.rand(3) #el random.rand genera numeros float aleatorios en el intervalo [0, 1).
    #El resultado de esta ultima parte, deberia tener la forma array([0.653, 0.234, 0.987]). Eso nos va a dar un color RGB aleatorio
      pelotas_nuevas.append(Pelotas(tipo, self.config))
    return pelotas_nuevas
