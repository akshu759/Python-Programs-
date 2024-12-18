#WAP to get factorial of a number
#using recursion function calling itself again and again
def factorial(n):
    if n ==0:
        return 1
    else:
        return n * factorial(n-1)
    
n=int (input("enter a number"))
ans=factorial(n) #calling function
print("Factorial of",n,"is",ans)



#n=5 fact=5*4*3*2*1=120 

    