# 완전탐색 하나씩
# 중복된 값은 없다고 문제에서 설명.
# 최소값의 값을 저장할 변수를 따로 설정
def solution(arr):
    #첫번째 숫자를 넣고 시작
    min_value = arr[0]
    if len(arr) == 1:
        return [-1]
    for i,j in enumerate(arr[1:]):
        if j < min_value:
            min_value = j     
    arr.remove(min_value)
    return arr