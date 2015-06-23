def fibonacci(n):
    """Returns the nth value of the Fibonacci series"""
    if (n == 0):
        return 0
    elif  (n == 1):
        return 1
    elif (n > 1):
         return (fibonacci(n -1) + fibonacci(n-2))

print(fibonacci(3))




def lucas(n):
    """Returns the nth value of the Lucas series"""

    if (n ==0):
        return(2)
    elif (n == 1):
        return(1)
    elif (n > 1):
        return(lucas(n - 1) + lucas(n - 2))

print(lucas(3))



def sum_series(n, x=0, y=1):
    """Returns both fibonacci and lucas numbers"""
    if (x == 0 and y == 1):
        return(fibonacci(n))
    if (x == 2 and y == 1):
        return(lucas(n))

print(sum_series(3, x=2, y=1))
print(sum_series(3))




