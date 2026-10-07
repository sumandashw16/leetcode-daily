def sumAndMultiply(s: str, queries: list[list[int]]) -> list[int]:
    MOD = 10**9 + 7
    s = list(map(int, list(s)))
    prefix_sum = [s[0]]
    dict = {}
    ans = []
    if s[0] == 0:
        dict[0] = []
    else:
        dict[0] = [s[0]]
    for i in range(1,len(s)):
        prefix_sum.append(prefix_sum[i-1] + s[i])
        if s[i] == 0:
            dict[i] = dict[i-1]
        else:
            dict[i] = dict[i-1] + [s[i]]
    
    for i,j in queries:
        if i != 0:
            length = len(dict[i-1])
            if len(dict[j][length:]) == 0:
                ans.append(0)
            else:
                num = int("".join(map(str, dict[j][length:])))
                p = (prefix_sum[j] - prefix_sum[i-1])
                ans.append((num * p)% MOD)
        else:
            if len(dict[j]) == 0:
                ans.append(0)
            else:
                num = int("".join(map(str, dict[j])))
                p = (prefix_sum[j])
                ans.append((num * p)% MOD)
    return ans

print(sumAndMultiply(s = "9876543210", queries = [[0,9]]))
