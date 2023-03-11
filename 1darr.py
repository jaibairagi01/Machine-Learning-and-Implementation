print("how many elements to store inside the array; ")
num = input()
arr=[]
print("\nEnter" , num , "Element;" , end="")
num = int(num)
for i in range (num):
    element = input()
    arr.append(element)
print("\nThe array elements are")
for i in range(num):
    print(arr[i], end="")