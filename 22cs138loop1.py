a=int(input("Start:"))
b=int(input("End:"))
e=[i for i in range(a,b+1,1) if i%2==0] 
o=[i for i in range(a,b+1,1) if i%2!=0]
k=len(e)
h=len(o)
print("even=",k,"odd=",h)
