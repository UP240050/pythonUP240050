#1.
x = 0
suma = 0
while x<=100:
    suma = suma + x
    x+=1
print('The sum of all numbers is :',suma)

#2.
print('\n')
l=0
sum=0
sum1=0
while l<=100:
    if(l%2!=0):
        sum= sum + l
    elif(l%2==0):
        sum1 = sum1 + l
    l+=1
print('The sum of all evens is:',sum1,'And the sum of all odds is:',sum)