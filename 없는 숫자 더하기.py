def solution(numbers):
    #결과 담을 answer를 0으로 초기화
    answer = 0
    #0은 더할 필요가 없어서 1~9까지 숫자만 확인
    for i in range(1,10):
        if i not in numbers:
            answer = answer + i
    return answer