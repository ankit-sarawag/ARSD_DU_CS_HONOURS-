#Write a program to check whether the given graph is complete. Represent the graph using the adjacency matrix representation

#function checking whether the graph is complete or not 
def checkGraph(graph):
    vertices=len(graph)  #number of vertices in the graph
    for i in range(1,vertices+1):
        for j in range(1,vertices+1):
            if i!=j and graph[i-1][j-1]==0:
                return False
    return True

def main():
    vertices=int(input("enter the number of vertices in the graph:")) #taking  number of vertices from the user
    graph=[]
    
    #loop to get 1 or 0 depending on whether the vertices are connected or not 
    for i in range(1,vertices+1):
        rows=[]
        for j in range(1,vertices+1):
            inputValue=int(input(f"enter 1 if the ({i},{j}) are connected otherwise 0:"))
            rows.append(inputValue)
        graph.append(rows)
    
    print("input graph is:\n",graph)
    completeGraph=checkGraph(graph)   #calling the function
    if completeGraph==True:
        print("The given graph is complete")
    else:
        print("The given graph is not complete")
main()