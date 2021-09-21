'''Las librerias necesarias 
   networkx,itemgetter,copy & groupby 
'''

import networkx as nx
from operator import itemgetter
import copy
from itertools import groupby
 
G =  nx.DiGraph()
G.add_nodes_from([i for i in range(0,9)])
G.add_edges_from([(0,1),(0,2),(0,4),(0,6),(0,5),(2,3),(2,4),(3,8),(4,3),(4,8),(4,7),(5,7),(5,8),(6,7),(7,8)])
G.edges[0, 1]["camino"] = 1
G.edges[0, 2]["camino"] = 4
G.edges[0, 4]["camino"] = -2
G.edges[0, 6]["camino"] = 5
G.edges[0, 5]["camino"] = 1
G.edges[2, 3]["camino"] = 3
G.edges[2, 4]["camino"] = 2
G.edges[3, 8]["camino"] = -4
G.edges[4, 3]["camino"] = 5
G.edges[4, 8]["camino"] = 1
G.edges[4, 7]["camino"] = 2
G.edges[5, 7]["camino"] = -1
G.edges[5, 8]["camino"] = -3
G.edges[6, 7]["camino"] = 6
G.edges[7, 8]["camino"] = 2

print(G.nodes)
print(G.edges)
print(G.nodes(data=True))
print(G.edges(data=True))

def max_edges(num, final_list = [],flag = True):
  if (len(list(G.successors(num))) != 0):
    for i in list(G.successors(num)):      
      final_list.append((i,1))
      max_edges(i,final_list,False)
    if flag:
        return final_list
  else:
    return final_list

org = 0
my_list = max_edges(org)
first = itemgetter(0)
sums = [(k, sum(item[1] for item in tups_to_sum))
        for k, tups_to_sum in groupby(sorted(my_list, key=first), key=first)]

sums

base = 0
winner = 0
for key, val in sums:
  if val > base:
    base = val
    winner = key
print("Vértice ( V) accesible por el mayor número de rutas procedente del vértice origen 0")
print("Ganador: ", winner, "  con ", base, "  rutas desde 0")

output = []
def path_weight(dest,org , path = "", weight = [0]):
  for n, nbrs in G.adj.items():
    for nbr, eattr in nbrs.items():
        if nbr == dest:
          #print(n,nbr,eattr)
          wc = weight.copy()
          wc.append(eattr["camino"])
          if n == org:
              path = path + " <- " + str(n)
              camino = sum(wc)
              output.append((path,camino))
          else:
              path_weight(n,org , copy.copy(path + " <- " + str(n)),wc)
  return output

output = path_weight(winner, org, str(winner))

size_list = len(output)
for i in range(0,size_list):
    for j in range(i,size_list):
        camino1 = output[i][1]
        camino2 = output[j][1]
        if camino2 > camino1:
          aux = output[i]
          output[i] = output[j]
          output[j] = aux

print("Imprimir y ordenar rutas costo descendente")
for path, val in output:
  print("Ruta: ", path, "camino: ", val)

print("V̀ es el vértice más accesible")

G.add_node("V̀")
G.add_edge(8, "V̀")
G.edges[8, "V̀"]["camino"] = 2

print(G.edges(data=True))

