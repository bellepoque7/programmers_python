from itertools import combinations
#메인함수
def solution(nums):
    answer = 0
    
    for combi in combinations(nums,3):
        answer = answer + check_prime(sum(combi))
        
    return answer

#소수 판별기 함수
def check_prime(num):
    # 숫자 1,0은 소수 아님
    if num == 1 or num == 0:
        return False
    # 그렇지않으면 2부터 num-1 까지 나누어 떨어지는 숫자 확인
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True