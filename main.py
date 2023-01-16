from grafo import Grafo

def separa():
  print()
  print("--------------------------------------------")
  print()


if __name__=='__main__':

  # Grafo 1
  g_1 = Grafo(4)
  
  print("Grafo 1")
  g_1.add_aresta(0,3)
  g_1.add_aresta(0,2)
  g_1.add_aresta(1,3)
  g_1.add_aresta(1,2)
  g_1.add_aresta(3,2)
  g_1.add_vertice()
  g_1.add_vertice()
  g_1.add_aresta(1,5)
  g_1.add_aresta(2,5)
  g_1.add_aresta(1,4)
  g_1.add_aresta(4,3)
  g_1.add_vertice()
  g_1.add_vertice()
  g_1.add_aresta(6,7)
  g_1.add_aresta(6,5)
  g_1.add_aresta(7,5)
  g_1.imprime_grafo()
  print()

  print("Cadeia Euleriana Grafo 1")
  g_1.algoritmo_hierholzer()
  separa()


  # Grafo 2
  g_2 = Grafo(8)
  
  print("Grafo 2")
  g_2.add_aresta(0,5)
  g_2.add_aresta(5,1)
  g_2.add_aresta(2,3)
  g_2.add_aresta(1,0)
  g_2.add_aresta(7,1)
  g_2.add_aresta(6,0)
  g_2.add_aresta(2,7)
  g_2.add_aresta(0,4)
  g_2.add_aresta(4,6)
  g_2.add_aresta(4,7)
  g_2.add_aresta(3,5)
  g_2.add_aresta(5,4)
  g_2.add_aresta(6,1)
  g_2.add_aresta(6,7)
  g_2.imprime_grafo()
  print()

  print("Cadeia Euleriana Grafo 2")
  g_2.algoritmo_hierholzer()
  separa()

  # Grafo 3
  g_3 = Grafo(9)
  
  print("Grafo 3")
  g_3.add_aresta(4,2)
  g_3.add_aresta(5,6)
  g_3.add_aresta(0,8)
  g_3.add_aresta(4,0)
  g_3.add_aresta(8,4)
  g_3.add_aresta(6,3)
  g_3.add_aresta(2,6)
  g_3.add_aresta(7,4)
  g_3.add_aresta(5,8)
  g_3.add_aresta(1,5)
  g_3.add_aresta(1,8)
  g_3.add_aresta(7,3)
  g_3.add_aresta(7,6)
  g_3.add_aresta(5,7)
  g_3.imprime_grafo()
  print()

  print("Cadeia Euleriana Grafo 3")
  g_3.algoritmo_hierholzer()
  separa()
  
"""
  g = Grafo(10)
  g.imprime_grafo()
  separa()

  print("verifica se possui ciclo")
  print(g.ciclo_euleriano())
  separa()
  
  print("remove aresta que conecta v3 e v2")
  g.remove_aresta(3,2)
  g.imprime_grafo()
  separa()
  
  print("remove v2")
  g.remove_vertice(2)
  g.imprime_grafo()
  separa()
  
  print("tenta adicionar aresta a vertice removido")
  g.add_aresta(0,2)
  g.imprime_grafo()
  separa()
  
  print("verifica o grau")
  print(g.grau(0))
  print(g.grau(3))
  separa()
  
  print("verifica os vizinhos")
  print(g.vizinhos(0, 3))
  print(g.vizinhos(0, 1))
  separa()
"""
