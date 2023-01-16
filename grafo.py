import copy

class Grafo:

  class Vertice():
        def __init__(self):
            self.valido = True
            self.vizinhos = []

  
  def __init__(self, n):
    self.n = n
    self.grafo = []
    for i in range(self.n):
      self.grafo.append(self.Vertice())

  
  def add_vertice(self):
    self.grafo.append(self.Vertice())
    self.n += 1


  def add_aresta(self, v, u):
    if self.grafo[v].valido and self.grafo[u].valido:
      self.grafo[v].vizinhos.append(u)
      self.grafo[u].vizinhos.append(v)

  
  def remove_aresta(self, v, u):
    self.grafo[v].vizinhos.remove(u)
    self.grafo[u].vizinhos.remove(v)

  
  def remove_vertice(self, v):
    if self.grafo[v].valido:
      for u in self.grafo[v].vizinhos:
        self.grafo[u].vizinhos.remove(v)
      self.grafo[v].valido = False
      self.grafo[v].vizinhos = []
      self.n -= 1

  
  def grau(self, v):
    if self.grafo[v].valido:
      return len(self.grafo[v].vizinhos)

  
  def vizinhos(self, v, u):
    if u in self.grafo[v].vizinhos:
      return True
    return False

  
  def ciclo_euleriano(self):
    visitados = [False] * self.n
    
    def busca_profundidade(v):
      if (self.grau(v) % 2) != 0:
        return
      visitados[v] = True
      for vizinho in self.grafo[v].vizinhos:
        if not visitados[vizinho]:
          busca_profundidade(vizinho)
          
    busca_profundidade(0)
    for visita in visitados:
      if not visita:
        return False
    return True
      
    
  def imprime_grafo(self):
    for i in range(self.n):
      if self.grafo[i].valido:
        print(i, end = " ")
        for v in self.grafo[i].vizinhos:
          print(f"-> {v}", end = " ")
      print()

  
  def algoritmo_hierholzer(self):
    grafo_copia = Grafo(0)
    grafo_copia.n = self.n
    grafo_copia.grafo = copy.deepcopy(self.grafo)
    
    def constroi_ciclo(vertice):
      ciclo_atual = [vertice]
      vizinho = grafo_copia.grafo[vertice].vizinhos[0]
      v_atual = vertice
      while vertice != vizinho:
        ciclo_atual.append(vizinho)
        grafo_copia.remove_aresta(v_atual, vizinho)
        v_atual = vizinho
        vizinho = grafo_copia.grafo[vizinho].vizinhos[0]
      grafo_copia.remove_aresta(v_atual, vertice)
      ciclo_atual.append(vertice)
      return ciclo_atual

    def junta_ciclos(ciclo_total, ciclo_atual):
      index = ciclo_total.index(ciclo_atual[0])
      ciclo = ciclo_total[:index] + ciclo_atual + ciclo_total[index+1:]
      return ciclo

    def encontra_vertice(ciclo_total):
      for v in ciclo_total:
        if grafo_copia.grau(v) > 0:
          return v

    def verifica_encerramento():
      for i in range(grafo_copia.n):
        if grafo_copia.grau(i) > 0:
          return True
      return False

    def imprime_ciclo(ciclo):
      for i in range(len(ciclo)-1):
          print(f"{ciclo[i]} ->", end = " ")
      print(ciclo[len(ciclo)-1])

    def cadeia_euleriana():
      if not grafo_copia.ciclo_euleriano():
        return
      ciclo = constroi_ciclo(0)
      imprime_ciclo(ciclo)
      vizinho = encontra_vertice(ciclo)
      while verifica_encerramento():
        ciclo_atual = constroi_ciclo(vizinho)
        imprime_ciclo(ciclo_atual)
        ciclo = junta_ciclos(ciclo, ciclo_atual)
        imprime_ciclo(ciclo)
        vizinho = encontra_vertice(ciclo)

    cadeia_euleriana() 
