import time

t0 = time.time()


def test(arr, k):
    arr_set = set(arr)
    for num in arr:
        if (17 - num) in arr_set:
            return True


print(test([10, 15, 3, 7], 17))

t1 = time.time()
print("Total Time", (t1 - t0))
