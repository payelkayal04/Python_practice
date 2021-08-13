A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def rotate_array_right_to_left(A):
    n = int(input("Enter the number of rotations"))
    for i in range(n):
        temp = A[len(A) - 1]         #save the last item in temp variable
        for j in range(len(A)-1, 0, -1):      #run this for loop backward from last element to first
            A[j] = A[j-1]      #Shift last value with it's prev value until it reaches to the first item.

        A[0] = temp
    print(A)
rotate_array_right_to_left(A)

B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#output = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
def rotate_array_left_to_right(B):
    n = int(input("Enter the number of rotations"))
    for i in range(n):
        temp = B[0]
        for j in range(0, len(B)-1):
            B[j] = B[j+1]
        B[len(B)-1] = temp
    print(B)


rotate_array_left_to_right(B)
