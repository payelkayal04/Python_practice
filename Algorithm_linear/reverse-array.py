arr = [1, 2, 3, 4, 5]
print("Original array:")
for i in range(len(arr)):
    print(arr[i], end=" ")
print("\nReverse array:")
for i in range(len(arr)-1, -1, -1):
    print(arr[i], end=" ")