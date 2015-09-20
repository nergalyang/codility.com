def solution(A):
    leftSum = A[0]
    rightSum = sum(A) - leftSum
    minDiff = abs(leftSum - rightSum)
    for i in range(1, len(A) - 1):
        leftSum += A[i]
        rightSum -= A[i]
        diff = abs(leftSum - rightSum)
        minDiff = min([minDiff, diff])
    return minDiff