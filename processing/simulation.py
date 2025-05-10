import pygame
import math
from processing.objetos import Objeto

class Simulacion:
  def __init__(self, objetos, config):
    self.objetos = objetos
    self.gravedad = config['simulacion']['gravedad']
    self.tiempo_simulacion = config['simulacion']['tiempo_simulacion']
    self.ancho = config['simulacion']['ancho']
    self.alto = config['simulacion']['alto']

  def gravitacion(self):
    self.radio_interaccion = config['simulacion']['radio_interaccion']
    for objeto_1 in self.objetos:
      for objeto_2 in self.objetos:
        if objeto_1 != objeto_2:
          dx = objeto_2.x - objeto_1.x
          dy = objeto_2.y - objeto_1.y
          distancia = math.sqrt(dx**2 + dy**2)
          if distancia < self.radio_interaccion:
            fuerza = self.gravedad * objeto_1.masa * objeto_2.masa / distancia**2
            objeto_1.velocidad_x += fuerza * dx / distancia
            objeto_1.velocidad_y += fuerza * dy / distancia

  def actualizar_posiciones(self):
      for objeto in self.objetos:
        objeto_1.x += objeto_1.velocidad_x
        objeto_1.y += objeto_1.velocidad_y

  def colision(self):
      nuevo_objetos = []#objetos nuveos
      for i, objeto_1 in enumerate(self.objetos):
         for j, objeto2 in enumerate(self.objetos):
           if i !=j and j:
             dx = objeto_2.x - objeto_1.x
             dy = objeto_2.y - objeto_1.y
             distancia = math.sqrt(dx**2 + dy**2)
             if distancia < self.radio_interaccion:
              masa_total = objeto_1.masa + objeto_2.masa
              xn = (objeto_1.x * objeto_1.masa + objeto_2.x * objeto_2.masa) / masa_total
              yn = (objeto_1.y * objeto_1.masa + objeto_2.y * objeto_2.masa) / masa_total
              vxn = (objeto_1.velocidad_x * objeto_1.masa + objeto_2.velocidad_x * objeto_2.masa) / masa_total #Del momento
              vyn = (objeto_1.velocidad_y * objeto_1.masa + objeto_2.velocidad_y * objeto_2.masa) / masa_total
              radio_nuevo = (objeto_1.radio + objeto_2.radio)/2
              tipo = objeto_1.tipo #tipo del objeto 1
              nuevo_objeto = Objeto(tipo, masa_total, xn, yn, vx, vy, radio_nuevo)
              nuevo_objetos.append(nuevo_objeto)
              break
         else:
           nuevo_objetos.append(objeto_1)

  self.objetos = nuevos_objetos
