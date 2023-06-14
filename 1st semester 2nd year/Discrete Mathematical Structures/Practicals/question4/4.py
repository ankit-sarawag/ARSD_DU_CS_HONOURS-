
#For any number n, write a program to list all the solutions of the equation x1+x2+x3+...+xn=C, where the constant (C<=10) and
#x1, x2, x3,...xn are nonnegative integers using brute force strategy.

def findSolutions(n,c):           #function calculating all the possible solutions for function
    solutions=[]                  #2-dimensional list storing the list of the availabe solutions
    for i in range(c+1):
        for j in range(c+1-i):
            for k in range(c+1-i-j):
                if i+j+k==c:      #checking if the current values of the variables satisfies the equation
                    solutions.append([i,j,k])
    
    return solutions

#main function
def main():
    n=int(input("enter the value for n:"))  #taking value of n from the user
    c=int(input("enter the value for c:"))  #taking value of c from the user
    solutions=findSolutions(n,c)  #calling the function
    print(f"solutions for x1 + x2 + x3 = {c}, where n={n}:")
    for i in solutions:
        print(i)

main()