import time

t0 = time.time()


def test(arr):
    length = len(arr)
    left = [None] * length
    right = [None] * length
    result = [None] * length

    left[0] = 1
    right[length - 1] = 1
    for i in range(1, length):
        left[i] = left[i-1] * arr[i-1]

    for i in range(length-2,-1,-1):
        right[i] = right[i+1] * arr[i+1]

    for i in range(0,len(left)):
        result[i] = left[i] * right[i]

    return result


print(test([1, 2, 3, 4, 5]))
print(test([3, 2, 1]))

t1 = time.time()
print("Total Time", (t1 - t0))
