num1=100
num2=20
x=0
if num1<num2:
    x=num1
if num2<num1:
    x=num2

for i in range(1,x+1):
    if num1%i==0 and num2%i==0:
        gcd=i
print(gcd)
