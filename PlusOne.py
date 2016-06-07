# Given a non-negative number represented as an array of digits,

# add 1 to the number ( increment the number represented by the digits ).

# The digits are stored such that the most significant digit is at the head of the list.

# Example:

# If the vector has [1, 2, 3]

# the returned vector should be [1, 2, 4]

# as 123 + 1 = 124.

# @param A : list of integers
# @return a list of integers
def PlusOne(A):
    remainder = 1

    for i in xrange(len(A) - 1, -1, -1):
        item = A[i]

        item += remainder

        if item > 9:
            A[i] = 0
            remainder = 1
        else:
            A[i] = item
            remainder = 0
            break

    if remainder:
        return [remainder] + A

    return A

print PlusOne([1, 2, 3])

print PlusOne([9, 9])
