from array import *
arr = array("i",[])
n = int(input("enter length of array : "))
for i in range(n):
    x = int(input("enter your number: "))
    arr.append(x)
print(arr)
val = int(input(" Enter the Number for index value : "))
k = 0
for e in arr:
    if e == val:
        print(k)
        break
    k = k+1
