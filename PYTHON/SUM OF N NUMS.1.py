def sumnum(n):
    if n <= 1:
        return n
    else:
        return n + sumnum(n-1)
n = int(input("Enter the value : "))

if n < 0:
    print("Enter a positive number")
else:
    print("The sum is" ,sumnum(n))
