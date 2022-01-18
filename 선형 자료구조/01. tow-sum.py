# 두 수의 합
"""
조건: 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""
# 브루트 포스: 배열을 2번 반복하면서 모든 조합을 더해서 일일이 확인해보는 무차별 대입 방식
# O(n^2)
def twoSum(self, nums:List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

# enumerate 함수
"""
>>> for entry in enumerate(['A', 'B', 'C']):
...     print(entry)
...
(0, 'A')
(1, 'B')
(2, 'C')
>>> for i, letter in enumerate(['A', 'B', 'C']):
...     print(i, letter)
...
0 A
1 B
2 C
"""
# 첫 번째 수를 뺀 결과 키 조회
def twoSum(self, nums:List[int], target: int) ->List[int]:
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i
    
    # 타겟에서 첫 번째 수를 뺀 결과로 키로 조회
    for i, num  in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return nums.index(num), nums_map[target - num]

# 조회 구조 개선
def twoSum(self, nums:List[int], target: int) ->List[int]:
    nums_map = {}
    # 하나의 for문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i

# 투 포인터 이용
"""
투 포인터: 왼쪽 포인터와 오른쪽 포인터의 합이 타겟보타 크면 오른쪽 포인터를 왼쪽으로,
작다면 왼쪽 포인터를 오른쪽으로 옮기는 방식
하지만, 투 포인터를 사용하려면 정렬을 해야하는데 정렬하면 인덱스가 달라짐 --> 문제의 의도와 맞지 않음
"""

