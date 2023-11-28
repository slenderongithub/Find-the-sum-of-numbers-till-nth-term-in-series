#WAP to to find the sum of numbers till nth term in series: 1+2+3+4....
n=int(input("Enter the number of terms: "))
s=0
for i in range(1,n+1):
    print(i,end="")
    if(i<n):
        print("+",end="")
    s=s+i
print("=",s)