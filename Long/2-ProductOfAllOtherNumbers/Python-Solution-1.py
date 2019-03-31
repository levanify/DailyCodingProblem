import time

t0 = time.time()


def test(arr):
    product = 1
    result = []
    for num in arr:
        product *= num

    for num in arr:
        result.append(product/num)

    return result


print(test([1, 2, 3, 4, 5]))
print(test([3, 2, 1]))

t1 = time.time()
print("Total Time", (t1 - t0))
