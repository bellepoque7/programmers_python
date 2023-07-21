def solution(a, b):

    # 날짜 전처리
    answer = ''
    # index월의 날짜 수(맨앞 0은 무시)
    days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    dates = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    
    days_2016 = sum(days)     
    dates_2016 = dates*(days_2016//7) + dates[:days_2016%7]

    # 들어오는 날짜를 정수화 
    date_to_int = sum(days[1:a]) + b
    answer = dates_2016[date_to_int-1]
     # 1일이 금요일, 2일이 토요일 .. 365일(마지막날) 금요일
    # for i in zip(range(1,days_2016+1,), dates_2016):
    #     print(i)
    # print(answer)
    return answer



import datetime

def getDayName(a,b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    return t[datetime.datetime(2016, a, b).weekday()]


#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(5,24))

