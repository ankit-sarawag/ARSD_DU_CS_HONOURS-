
# write a program to evaluate a polynomial function
def evaluatePolynomial(coefficients,value):   #function for calculating the polynomial function value
    result=0
    power=len(coefficients)-1
    for i in coefficients:     #traversing the coefficients
        result+=i*(value**power)
        power-=1
    return result             #returning the value of the polynomial function


def main():          #main function
    degree=int(input("enter the degree of your polynomial function:"))        #degree of the polynomial
    coefficients=[]           #list storing the coefficients
    for i in range(degree,-1,-1):
        if i!=0:
            n=int(input("enter the coefficient of x^^{}:".format(i)))  #taking value of the coefficients from the user
        else:
            n=int(input("enter the value of the constant term:"))
        coefficients.append(n)
    
    #value for which to calculate the polynomial function
    n=int(input("enter the value for which you want to evaluate the value of the polynomail function:"))
    polynomialValue=evaluatePolynomial(coefficients,n)
    print("the value of f(n)=",polynomialValue)
main()