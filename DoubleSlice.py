def solution(A):
    N = len(A)
    result = 0
    max_ending_temp = 0
    max_begining_temp = 0
    max_ending_here = [0]*N
    max_begining_here = [0]*N
    for i in xrange(1,N-1):
        max_ending_temp = max(A[i],max_ending_temp+A[i])
        max_ending_here[i] = max_ending_temp
    for k in xrange(N-2,0,-1):
        max_begining_temp = max(A[k],max_begining_temp+A[k])
        max_begining_here[k] = max_begining_temp
    for i in xrange(0,N-2):
        result = max(result,max_ending_here[i]+max_begining_here[i+2])
    return result