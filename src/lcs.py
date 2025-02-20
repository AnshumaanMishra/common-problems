s1 = "pmjghexyb"
s2 = "hafcdqbgn"
xl = len(s1)
yl = len(s2)
memo = [[0 for _ in range(len(s2))] for _ in range(len(s1))]
memo2 = [['' for _ in range(len(s2))] for _ in range(len(s1))]

def fillMemo(x, y):
    print(x, y, memo)
    if(s1[x] == s2[y]):
        if(x * y != 0):
            memo[x][y] = 1 + fillMemo(x - 1, y - 1)[0]
            memo2[x][y] = fillMemo(x - 1, y - 1)[1] + s1[x]
        else:
            memo[x][y] = 1
            memo2[x][y] = s1[x]
        
    elif(x == 0 and y == 0):
        memo[x][y] = 0
        memo2[x][y] = ""
    elif(x == 0):
        a = fillMemo(x, y - 1)
        memo[x][y] = a[0]
        memo2[x][y] = a[1]
    elif(y == 0):
        a = fillMemo(x - 1, y)
        memo[x][y] = a[0]
        memo2[x][y] = a[1]
    else:
        a = fillMemo(x - 1, y)
        b = fillMemo(x, y - 1)
        memo[x][y] = max(a[0], b[0])
        if(a[0] > b[0]):
            memo2[x][y] = a[1]
        else:
            memo2[x][y] = b[1]
    return memo[x][y], memo2[x][y]



fillMemo(xl - 1, yl - 1)

print(*memo, sep="\n")
print(*memo2, sep="\n")


# def longestCommonSubsequence(text1: str, text2: str) -> int:
#     def fillMemo(x, y, s1, s2, memo2):
#         # print(x, y)
#         if(s1[x] == s2[y]):
#             memo2[x][y] = fillMemo(x - 1, y - 1, s1, s2, memo2)[1] + s1[x]
#         elif(x == 0 and y == 0):
#             memo2[x][y] = ""
#         elif(x == 0):
#             a = fillMemo(x, y - 1, s1, s2, memo2)
#             memo2[x][y] = a
#         elif(y == 0):
#             a = fillMemo(x - 1, y, s1, s2, memo2)
#             memo2[x][y] = a
#         else:
#             a = fillMemo(x - 1, y, s1, s2, memo2)
#             b = fillMemo(x, y - 1, s1, s2, memo2)
#             if(len(a) > len(b)):
#                 memo2[x][y] = a[1]
#             else:
#                 memo2[x][y] = b[1]
#         return memo2[x][y]
#     xl = len(text1)
#     yl = len(text2)
#     # memo = [[0 for _ in range(len(text2))] for _ in range(len(text1))]
#     memo2 = [['' for _ in range(len(text2))] for _ in range(len(text1))]
#     fillMemo(xl - 1, yl - 1, text1, text2, memo2)
#     return memo2[xl - 1][yl - 1]


# print(longestCommonSubsequence(s1, s2))



