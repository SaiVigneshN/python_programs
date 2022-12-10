print('Enter input')
n=int(input())
for i in range(0,n):
    for j in range(0,i+1):
        print('#',end='')
    print()

print('------------------------------------------------------')

count=0
total=0
n=int(input('Enter the number of subjects'))
while count<n:
    mark=int(input('Enter mark:'))
    if mark<0:
        print("Mark should be gfrater than 0")
        break
    total=total+mark
    count=count+1
else:
    average=total/n
    print("Average:",average)
