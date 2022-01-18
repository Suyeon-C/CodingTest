"""
한번의 거래로 낼 수 있는 최대 이익을 산출하라.
Input: prices= [7,1,5,3,6,4]
Output: 5
"""

# 브루트 포스로 계산  O(n^2)------! 러너타임 에러
def maxProfit(self, prices:List[int]) -> int:
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)
    
    return max_price

# 저점과 현재 값과의 차이 계산: 카데인 알고리즘, O(n)
def maxProfit(self, prices:List[int]) -> int:
    profit = 0
    min_price = sys.maxsize # python3에서 int의 최댓값

    # 최솟값과 최댓값을 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit