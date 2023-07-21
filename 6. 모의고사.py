def solution(answers):
    stu_1 = [1, 2, 3, 4, 5]
    stu_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    stu_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    stu_cnt = [0,0,0] 
    i = 0
    while i != len(answers) :
        if answers[i] == stu_1[i%len(stu_1)]:
            stu_cnt[0] = stu_cnt[0] + 1
        if answers[i] == stu_2[i%len(stu_2)]:
            stu_cnt[1] = stu_cnt[1] + 1
        if answers[i] == stu_3[i%len(stu_3)]:
            stu_cnt[2] = stu_cnt[2] + 1
        i = i + 1
    answer = find_max_index(stu_cnt)
    return answer
def find_max_index(lst):
    for _ in lst:
        answer = []
        max_value = max(lst)  # 리스트 내 가장 큰 값 구하기
        answer.extend([index + 1for index, value in enumerate(lst) if value == max_value])
    return answer
# solution([1,3,2,4,2])