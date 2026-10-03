prices = [3,2,1]
def maxProfit(prices: list[int]) -> int:
    new_list = [(prices[i] - prices[i-1]) for i in range(1,len(prices))]
    if len(new_list) == 1 and new_list[0]>0:
        max_known = new_list[0]
    else:
        max_known = 0
    if len(new_list) == 0:
        return max_known
    else:
        curr_sum = new_list[0]
        max_known = new_list[0]
    for i in new_list[1:]:
        if curr_sum + i < i:
            curr_sum = i
        else:
            curr_sum += i
    
    return max(0,max_known)
print(maxProfit(prices))