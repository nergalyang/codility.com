def solution(A, X, D):
    N = len(A)
    currentpos = 0
    countList = [] #record postitons larger than currentpostion
    topop = []
    for i in xrange(N):
        if A[i] not in countList:
            countList.append(A[i])
        if 0 < (A[i]-currentpos) <= D:
            currentpos = A[i]
        #remove positions smaller than currentpostion
        for p in range(len(countList)):
            if countList[p] < currentpos:
                topop.append(countList[p])
        for ele in topop:
            countList.remove(ele)
        topop = []
        countList.sort()
        for items in countList:
            if currentpos>= (X-D):
                return i
                break
            if 0 < items- currentpos <= D:
                currentpos = items
                if currentpos >= (X-D):
                    return i
                    break
    return -1