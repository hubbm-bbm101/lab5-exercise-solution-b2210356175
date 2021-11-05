# exercise 1
def sum_odd_number(N):
    sum= 0
    for n in range(1, N+1):
        if (n & 2!=0):
            #print("debug odd" ,n)
            sum= sum + n
     return sum

def avg_even_number(N):
    sum= 0
    for n in range(1, N+1):
        if (n % 2==0)
            #print("debug even", n)
            sum= sum + n
    return sum/N

i=int(input("Please enter a number:"))
print("first calculation", sum_odd_number(i))
print("second calculation", avg_even_number(i))

