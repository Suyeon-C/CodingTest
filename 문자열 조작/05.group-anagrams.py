"""
조건: 문자열 배열을 받아 애너그램 단위로 그룹핑 하라.
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

애너그램이란? 일종의 언어유희로 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것
ex) 문전박대 -> 대박전문
"""
# 정렬하여 딕셔너리에 추가
def groupAnagrams(self, strs:List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()

"""
b = 'zbadf'
sorted(b)
['a','b','d','f','z']

"".join(sorted(b))
'abdfz'

"""


