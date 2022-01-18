# 유효한 팰린드롬
"""
팰린드롬 = 앞 뒤가 똑같은 단어나 문장 ex)소주 만 병만 주소 
예제)
조건: 주어진 문자열이 팰린드롬인지 확인하여라. 대소문자는 구분x, 영문자와 숫자만을 대상 
입력: "A man, a plan, a canal: Panama"
출력 : true
"""
# 리스트로 변환 Runtime: 32 ms
def isPalindrome1(self,s:str) -> bool:
    strs = [] # 리스트 선언
    for char in s:
       if char.isalnum(): #islnum: 영문자,숫자 여부를 판별하는 함수 
          strs.append(char.lower())
    while len(strs) > 1: #팰린드롬 여부 판별
        if strs.pop(0) != strs.pop(): #pop(0)은 맨 앞, pop()은 마지막, O(n^2), O(n)
                return False
    return True

# 데크 자료형을 이용한 최적화 
def isPalindrome2(self,s:str) -> bool:
    strs : Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    while len(strs) > 1:
        if strs.popleft() != strs.pop(): # O(1), 데크 구현 O(n), O(1)
            return False

    return True

# 슬라이싱 이용
def isPalindrome(self, s:str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]','',s)

    return s == s[::-1] # 슬라이싱 

