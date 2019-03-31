import time

t0 = time.time()


def test(arr):
    left = []
    right = []
    result = []
    for i in range(0,len(arr)): # Loop from beginning to last index
        left_product = 1
        right_product = 1
        if i == 0:
            left_product = 1
        else:
            for j in range(0,i):
                left_product *= arr[j]

        if i == len(arr) - 1:
            right_product = 1
        else:
            for j in range(i+1,len(arr)):
                right_product *= arr[j]

        left.append(left_product)
        right.append(right_product)

    for i in range(0, len(left)):
        result.append(left[i] * right[i])

    return result


print(test([1, 2, 3, 4, 5]))
print(test([3, 2, 1]))

t1 = time.time()
print("Total Time", (t1 - t0))
