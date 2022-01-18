"""
가장 긴 팰린드롬 부분 문자열을 출력하라.
Input: s = "babad"
Output: "bab"
"""

#중앙을 중심으로 확장하는 풀이
def longestPalindrome(self, s:str) -> str:
    #팰린드롬 판별 및 투 포인터 확장
    def expend(left: int, right:int) -> str:
        while left >= 0 and right <= len(s) and s[left] == s[right-1]:
            left -= 1
            right += 1
            return s[left + 1:right -1]

    # 해당 값이 없을 때, 빠르게 리턴 
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    
    #슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) -1):
        result = max(result,
                            expend(i,i + 1),
                            expend(i,i + 2),
                            key=len) #key=len을 추가하면 단어들이 길이순으로 정렬
    return result
