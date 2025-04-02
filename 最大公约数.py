x = int(input())
y = int(input())
while y%x!=0:
    y,x = x,y%x
print(x)
