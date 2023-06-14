#Write a program to check whether the given graph is complete. Represent the graph using the adjacency list representation

#function checking whether the graph is complete or not 
def checkGraph(graph):
    vertices=len(graph)                #number of vertices in the graph
    #loop to check if each vertex is connected to all other vertices
    for i in range(1,vertices):
        neighbours=graph[i]
        if len(neighbours)!=vertices -1:
            return False
    return True


def main():
    vertices=int(input("enter the number of vertices in the graph:")) #taking  number of vertices from the user
    graph=[]
    
    #loop to get the neighbours of the vertices
    for i in range(1,vertices+1):
        rows=[]
        neighbours=eval(input(f"enter the neighbours for vertex {i}:"))
        graph.append(neighbours)
    
    print("input graph is:\n",graph)
    completeGraph=checkGraph(graph)   #calling the function
    if completeGraph==True:
        print("The given graph is complete")
    else:
        print("The given graph is not complete")
main()
