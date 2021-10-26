# Armstrong Number

n=input("Enter a number: ")
total_sum=0
for i in n:
    initial_sum=int(i)**3
    total_sum+=initial_sum
print(total_sum)
if int(n)==total_sum:
    print("{} is an Armstrong number".format(n))
else:
    print("{} is not an Armstrong number".format(n))
