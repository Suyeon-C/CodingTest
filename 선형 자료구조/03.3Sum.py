"""
배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""

# 브루트 포스로 계산  --> 중복 x , 오류 뜸
def threeSum(self, nums:List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    length = len(nums)
    for i in range(length - 2):
        # 중복 값 건너 뛰기 
        if nums[i] > 0 or (i > 0 and nums[i] == nums[i-1]):
            continue
        for j in range(i + 1, length - 1):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            for k in range(j + 1, length):
                if k > j + 1 and nums[k] == nums[k-1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append((nums[i], nums[j], nums[k]))

    return result

# 투 포인터로 합 계산
def threeSum(self, nums:List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    for i in range(len(nums)-2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i -1]:
            continue
        # 간격을 좁혀가며 합 sum 계산
        left, right = i+1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # sum = 0 인 경우이므로 정답 및 스킵 처리
                results.append((nums[i], nums[left], nums[right]))

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return results




