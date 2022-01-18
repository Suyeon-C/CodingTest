# 문자열 뒤집기
"""
조건: 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 내부를 직접 조작하라
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""
# 투 포인터를 이용한 스왑 
# 투 포인터: 2개의 포인터를 이용해 범위를 조정해가며 풀이하는 방식
def reverseString(self, s:List[str]) -> None:
    left, right = 0, len(s) -1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# 파이썬 다운 방식
def reverseString(self, s:List[str]) -> None:
    s.reverse() # reverse() 함수는 리스트에서만 제공 
   # s[:] = s[::-1]

