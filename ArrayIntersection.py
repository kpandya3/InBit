# Given two arrays, write a function to compute their intersection.

def intersection(arr1, arr2):
    data = {}
    res = []

    for i in arr1:
        if i in data:
            data[i] += 1
        else:
            data[i] = 1

    for i in arr2:
        if i in data and data[i] > 0:
            res.append(i)
            data[i] -= 1

    return res

print intersection([1, 2, 2, 1], [2, 2])
