
#Write a program to accept a directed graph G and compute the in-degree and out-degree of each vertex
def Degrees(graph):
    vertices=len(graph)      #number of vertices in the graph
    inDegrees=[0]*vertices      #list for indegrees of the vertices
    outDegrees=[0]*vertices     #list for outdegrees of the vertices

    #loop computing the in-degrees and out-degrees of the graph
    for i in range(vertices):
        for j in range(vertices):
            if graph[i][j]==1:
                inDegrees[j]+=1
                outDegrees[i]+=1
    return inDegrees,outDegrees
            
def main():
    vertices=int(input("enter the number of vertices in the graph:")) #taking  number of vertices from the user
    graph=[]
    
    #loop to get 1 or 0 depending on whether the vertices are connected or not 
    for i in range(1,vertices+1):
        rows=[]
        for j in range(1,vertices+1):
            inputValue=int(input(f"enter 1 if the vertex ({j}) is connected from the vertex ({j}) otherwise 0:"))
            rows.append(inputValue)
        graph.append(rows)
    
    print("input graph is:\n",graph)
    inDegrees,outDegrees=Degrees(graph)   #calling the function
    for i in range(len(graph)):
        print(f"vertex ({i+1}): in-degree = {inDegrees[i]}, out-degree = {outDegrees[i]}")
main()