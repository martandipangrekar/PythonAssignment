def Hur(n):
    k=n-1
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k=k+1
        for i in range(0,i+1):
            print("*",end=" ")
        print()
    k=2*n-1
    for i in range(0,n+1):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for i in range(0,i+1):
            print("-", end=" ")
        print()
n=int(input("Enter the number :"))
if n==2:
    Hur(n)
elif n==1:
    k = n - 1
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for i in range(0, i + 1):
            print("*", end=" ")
        print()
else:
    print("Invalid Input..")