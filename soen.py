#1
number=int(input())
output=''
even=''
a=len(str(number))
b=0
while a:
    c=str(number)
    if int(c[b])%2==0:
        even=even+c[b]
    else:
        output=output+c[b]
    b=b+1
    a=a-1
output=output+even
print(output)

#2
number1=int(input())
output1=''
times=len(str(number1))
index1=0
while times:
    f=str(number1)
    e=str(f[index1])
    if int(e)%2==0:
        output1=output1+'X'
    else:
        output1=output1+e
    index1=index1+1
    times=times-1
print(output1)
