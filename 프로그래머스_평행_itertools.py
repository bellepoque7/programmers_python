# 이중 반복문
# 임의의 두 점을 이은 직선이 x축 또는 y축과 평행한 경우는 주어지지 않습니다.
# -> 기울기 계산시 x,y가 0이되는 경우는 고려않음. 특히 divion by zero 조건분기 필요없음.

# 또한 문제는 4C3 점의 기울기를 구하는게 아니라
# 네개의 점을 두개씩(그러니까 모든 4개의 점을 다써서) 기울기를 구해야함.
from itertools import combinations
def solution(dots):
    # 4개의 점을 2개씩 짝지어 기울기를 구할수 있는 모든 경우의 수 3가지
    # (1번-2번, 3번-4번), (1번-3번, 2번-4번), (1번-4번, 2번-3번)
    dot_combi = list(combinations(dots,4))
    print(dot_combi)
    d1 = dot_combi[0][0]
    d2 = dot_combi[0][1]
    d3 = dot_combi[0][2]
    d4 = dot_combi[0][3]
    if cal_clin(d1,d2) == cal_clin(d3,d4):
        return 1
    elif cal_clin(d1,d3) == cal_clin(d2,d4): 
        return 1
    elif cal_clin(d1,d4) == cal_clin(d2,d3):
        return 1
    else:
        return 0
       

def cal_clin(dots_1, dots_2):
    # y값의 차 / x값의 차이 
    return (dots_2[1] - dots_1[1])/(dots_2[0] - dots_1[0])