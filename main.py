import networkx as nx
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import random
import math

def warshall(R,n,k,i,j):
    if(k==n or i==n or j==n):
        return

    if(R[i][j]or(R[i][k]and R[k][j])):
        R[i][j]=1

    warshall(R, n, k, i, j+1)
    warshall(R, n, k, i+1, j)
    warshall(R, n, k+1, i, j)

    return R

def show_Graph(y,R,G,name):
    plt.figure(name)
    for i in range(y):
        G.add_node(i + 1)

    for i in range(y):
        for j in range(y):
            if (R[i][j] == 1):
                G.add_edge(i + 1, j + 1)

    M = G.number_of_edges()
    edge_colors = range(2, M + 2)
    edge_alphas = [(5 + i) / (M + 4) for i in range(M)]
    cmap = plt.cm.plasma
    seed = 13648
    pos = nx.spring_layout(G, seed=seed)

    nx.draw_networkx(G, pos, with_labels=True, node_color="green")
    edges = nx.draw_networkx_edges(
        G,
        pos,
        edge_color=edge_colors,
        edge_cmap=cmap,
    )


def printList(R,name):
    df = pd.DataFrame(R)
    writer = pd.ExcelWriter(str(name)+'.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='welcome', index=False)
    writer.save()


y=int(input("Kaç eleman olacak:"))
z=int(input("İlişki yüzdesi:"))

d=math.floor((y*y)*(z/100.0))

R0=[]

for i in range(y):
    temp=[]
    for j in range(y):
        temp.append(0)
    R0.append(temp)

while(d>0):
    randX=random.randint(0, y-1)
    randY = random.randint(0, y-1)
    if(R0[randX][randY]==0):
        R0[randX][randY]=1
        d=d-1

print("R0:", R0)

G = nx.MultiDiGraph(directed=True)
show_Graph(y,R0,G,"İlk Durum")
printList(R0,"R0")

R=warshall(R0,y,0,0,0)

print("R:", R)

T = nx.MultiDiGraph(directed=True)
show_Graph(y,R,T,"Son Durum")
printList(R,"R")

plt.show()


