def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 


#factorial program. 
n = input("Enter a number: ")
factorial = 1
if int(n) >= 1:
    for i in range (1,int(n)+1):
        factorial = factorial * i
print("Factorail of ",n , " is : ",factorial)

