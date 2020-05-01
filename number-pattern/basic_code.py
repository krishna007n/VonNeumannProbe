n=int(input("Function 2^n : Enter the n value >>> "))
l=[1]
for m in range(n):
  c=max(l)
  z=l
  prev=1
  for i in z[:]:
    c=c-1 if i!=prev else c
    prev=i
    l.append(c+i)
print(l)
print("Length=2^"+str(n)+":"+str(len(l)))
