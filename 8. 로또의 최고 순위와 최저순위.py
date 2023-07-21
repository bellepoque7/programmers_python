# 방법1: 모든 경우의 수를 다 구해서 체크한다
# 방법2: 작성한 번호와 당첨번호의 교집합과 작성한 0번호를 센 후  최대,최소를 구한다.


lottos = [44, 7, 2, 3, 5, 25]
win_nums = [31, 10, 45, 1, 6, 19]
def solution(lottos, win_nums):
    zero_cnt = lottos.count(0)
    lottos_set = set(lottos)
    win_nums = set(win_nums)
    inter = list(lottos_set.intersection(win_nums))
    # 순위 + 맞은숫자 = 7(일정)
    # 단, 모두 틀렸을 경우 7이아닌 6으로 분기설정 필요
    # 2개의 교집합이 있고 0이 2개면, 최소 2개맞고 최대 4개맞을 수있음
    answer = []

    #최대로 맞출 등수
    answer.append(7 - len(inter) -  zero_cnt)
    #최소로 맞출 등수
    answer.append(7 - len(inter))


    # 1. 작성한 번호가 모두 0이면, 최악은 모두 틀려 6등인 경우
    if zero_cnt == 6:
        answer.pop()
        answer.append(6)
    # 2. 작성한 숫자와 당첨번호가  모든 숫자가 다르다면, [6,6]
    elif not lottos_set.intersection(win_nums) :
        answer = [6,6]
    return answer
solution(lottos, win_nums)