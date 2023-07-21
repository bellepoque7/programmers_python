def solution(x, n):
    answer = []
    # range(start,end,step)
    # start부터 end-step 까지 반환, 단 step = 0 d이면 에러 
    if x == 0 :
        return [0]*n
    for i in range(x,x*(n+1),x):
        answer.append(i)
    return answer