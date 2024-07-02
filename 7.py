n=int(input("Enter the Size of the cardPoints:"))
print("enter the Elements:")
a=[]
for i in range(n):
    a.append(int(input()))
m=int(input("Enter the k value:"))
b=[]
l=len(a)
c1=0
c2=0
for i in range(l-1,-1,-1):
    b.append(a[i])
for i in range(m):
    c2+=b[i]
for i in range(m):
    c1+=a[i]
if c1>c2:
    print(c1)
elif c1<c2:
    print(c2)
else:
    print(c1)
        
    
