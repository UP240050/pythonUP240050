#1.
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers: 
    print(number)   

count = 0
while count < 10:
    print(count)
    count = count + 1
else:
    print(count)

#2.
numbers1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for number in numbers1:
    print (number)

countt = 10
while count > 0:
    print(count)
    count = count - 1

#3.
for l in range(0,8,+1):
    print('#'*l)

#4.
print('\n')
for o in range(0,8):
    print('#  '*8)

#5.
print('\n')
for k in range(0,11):
    print(k, 'x', k, '=',(k*k))

#6.     
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in lst:
    print(item)

#7.
print('\n')
for x in range(0,101):
    if (x%2==0):
        print(x)

#8.
print('\n')
a=0
while a<=100:
    if(a%2!=0):
        print(a)
    a+=1