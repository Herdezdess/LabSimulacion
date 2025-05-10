import numpy as np

class Distribucion():
  def _init_(self, N:int=None):
    self.N_ = N #aquí definimos que N sean los elementos que se generan
  #para el proyecto se nos pide una distribución normal y una uniforme
  def distribucion_normal(self, media:float = 0.0, desviacion:float=0.0):
    dist = np.random.normal(media, desviacion, self._N)
    return dist

  def distribucion_uniforme(self, media:float = 0.0, desviacion:float = 0.0):
    dist = np.random.normal(media, desviacion, self._N)
    return dist
  
  #set nosdevuelve datos aleatorios, dependiendo de la distribución
  def set(self, valor_inicial:float=None, valor_final:float=None, distribucion:str=""):
        try:
            if distribucion=="normal":
                var = self._normal_distribution(valor_inicial, valor_final)
            elif distribucion=="uniform":
                var = self._uniform_distribution(valor_inicial, valor_final)
            else:
                raise Exception("No hay distribucion")
            return var
        except Exception as e:
            print(f"Error: {e}")

    
