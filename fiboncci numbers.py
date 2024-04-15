pre=0
new=1
print(pre)
print(new)
pre=0
new=1


for i in range (0,17):
    next=pre+new
    pre=new
    new=next
    print(next)


        