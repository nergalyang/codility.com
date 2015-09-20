# Write a function:

# def solution(A)

# that, given a non-empty zero-indexed array A of N integers, returns the minimal positive integer (greater than 0) that does not occur in A.

# For example, given:

#   A[0] = 1
#   A[1] = 3
#   A[2] = 6
#   A[3] = 4
#   A[4] = 1
#   A[5] = 2
# the function should return 5.

# Assume that:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
# Complexity:

# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
# Elements of input arrays can be modified.


def solution(A):
    N = len(A)
    list = [False] * (N+1)
    for ele in A:
        if 1 <= ele <= N:
            list[ele] = True
    for k in range(1,N+1):
        if list[k] == False:
            return k
    return N+1
    