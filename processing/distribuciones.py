#distribuciones.py
import numpy as np

class Distribuciones:
  def _init_(self, N:int=None):
    self.N_ = N
  @staticmethod
  def gaussiana(self, media:float = 0.0, desviacion:float=0.0):
    dist = np.random.normal(media, desviacion, self._N)
    return dist
  @staticmethod
  def uniforme(valor_minimo:float = 0.0, valor_maximo:float = 0.0):
    dist = np.random.uniform(valor_minimo, valor_maximo, self._N)
    return dist

    
