# Factorial
            
n=int(input("Enter a number: "))
if n==1 or n==0:
    print(f"Factorial {n} is 1")
else:
    f=1
    for i in range(1,n+1):
        f=f*i
print("Factorial of {} is {}.".format(n, f))
