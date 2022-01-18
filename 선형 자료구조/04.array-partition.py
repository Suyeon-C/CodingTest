"""
n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라
Input: nums = [1,4,3,2]
Output: 4
"""

# 오름차순 풀이
from tkinter import N


def arrayPairSum(self, nums:List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum

# 짝수 번째 값 계산
def arrayPairSum(self, nums:List[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        # 짝수 번째 값의 합 계산
        if i % 2 == 0:
            sum += n 
    
    return sum

# 파이썬다운 방식
def arrayPairSum(self, nums:List[int]) -> int:
    return sum(sorted(nums)[::2])