import numpy as np

class Distribucion():
  def _init_(self, N:int=None):
    self.N_ = N #aquí definimos que N sean los elementos que se generan
  #para el proyecto se nos pide una distribución normal y una uniforme
  def distribucion_gaussiana(self, media:float = 0.0, desviacion:float=0.0):
    dist = np.random.normal(media, desviacion, self._N)
    return dist

  def distribucion_uniforme(self, media:float = 0.0, desviacion:float = 0.0):
    dist = np.random.normal(media, desviacion, self._N)
    return dist
  
  #set nosdevuelve datos aleatorios, dependiendo de la distribución
  def set(self, valor_inicial:float=None, valor_final:float=None, distribucion:str=""):
        try:
            if distribucion=="normal":
                dist = self._distribucion_gaussiana(valor_inicial, valor_final)
            elif distribucion=="uniform":
                dist = self._distribucion_uniforme(valor_inicial, valor_final)
            else:
                raise Exception("No hay distribucion")
            return dist
        except Exception as e:
            print(f"Error: {e}")

    
