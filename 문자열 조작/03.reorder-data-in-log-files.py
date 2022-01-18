# 로그 파일 재정렬
"""
조건: 로그의 가장 앞 부분은 식별자이다.
     문자로 구성된 로그가 숫자 로그보다 앞에 온다.
     식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
     숫자 로그는 입력 순서대로 한다.
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
"""
#람다와 +연산자 이용
def reorderLogFiles(self, logs:List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    #2개의 키를 람다 표현식으로 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0])) #x.split()[1:]이 동일한 경우 x.split()[0]으로 정렬
    return letters + digits