#현재 숫자를 저장하는 변수를 생성
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in arr[1:]:
        if answer[-1] == i:
            pass
        else:
            answer.append(i)
    return answer