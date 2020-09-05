i=1
while i<=5:
    print(i)
    i=i+1

print("finished!")

x=1
while x<10:
    if x%2 ==0:
        print(str(x)+" is even")
    else:
        print(str(x)+" is odd")
    x+=1

j=0
while True:
    print(j)
    j=j+1
    if j>=5:
        print("breaking")
        break
print("finished")

d=1
while d<=5:
    print(i)
    d+=1
    if d==3:
        print("skipping 3")
        continue