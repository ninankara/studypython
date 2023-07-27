def solution(n):
    answer = [[]]
    number = []
    numIdx = 0
    top = left = 0
    bottom = right = n-1
    
    for i in range(1,n*n+1): #n=3
        number.append(i)
    answer = [[0 for i in range(n)] for j in range(n)]
    
    while(True):
        if (left > right):
            break

        #print top row
        for i in range(left,right+1): #00 01 02
            answer[top][i] = number[numIdx]
            numIdx += 1
        top +=1 #increase top index

        if (top > bottom):
            break
    
        #print right column
        for i in range(top, bottom+1):
            answer[i][right] = number[numIdx]
            numIdx += 1
        right -=1 #decrease right idx

        if (left > right):
            break;
    
        #print bottom row
        for i in range(right,left-1,-1):
            answer[bottom][i] = number[numIdx]
            numIdx += 1
        bottom -= 1

        if (top>bottom):
            break
        
        ##print left column
        for i in range(bottom,top-1,-1):
            answer[i][left] = number[numIdx]
            numIdx +=1
        left +=1


    return answer

