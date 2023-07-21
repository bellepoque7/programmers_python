
def solution(nums):
    #중복제거한 숫자가 가져갈수 있는 숫자보다 많으면
    # 가져갈 수 있는 최대값 반환
    if len(set(nums)) >= len(nums)//2:
        return len(nums)//2
    # 그렇지 않으면 그냥 중복제거한 값 반환
    else: 
        return len(set(nums))