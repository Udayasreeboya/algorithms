# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# diagonal=[]
# anti_diagonal=[]
# for i in range(len(matrix)):
#     diagonal.append(matrix[i][i])
#     anti_diagonal.append(matrix[i][len(matrix)-i-1])

# print(diagonal)
# print(anti_diagonal)

# #make antidiagonal with 0s
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if i+j==len(matrix)-1:
#             matrix[i][j]=0
# print(matrix)

# #transpose of a matrix
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         matrix[i][j]=matrix[j][i]
# print(matrix)

# a="this is a sentence udayasree"
# b=a.split(" ")
# max_word=""
# for i in range(len(b)):
#     if len(max_word)<len(b[i]):
#         max_word=b[i]
# print(max_word)

# def exist(board,word):
#     rows=len(board)
#     cols=len(board[0])
#     def dfs(r,c,i):
#         if i==len(word):
#             return True
#         if r<0 or c<0 or r>=rows or c>=cols:
#             return False
#         if board[r][c]!=word[i]:
#             return False
#         temp=board[r][c]
#         board[r][c]="*"
#         found= (
#             dfs(r+1,c,i+1)or
#             dfs(r-1,c,i+1)or
#             dfs(r,c+1,i+1)or
#             dfs(r,c-1,i+1)
#         )
#         board[r][c]=temp
#         return found
#     for i in range(rows):
#         for j in range(cols):
#             if dfs(i,j,0):
#                 return True
#     return False
# board=[["a","b","c","e"],["s","f","c","s"],["a","d","e","e"]]
# word1="abcced"
# word2="abbcde"
# print(exist(board,word1))
# print(exist(board,word2))

# def is_valid(s):
#     stack=[]
#     mapping={")":"(","}":"{","]":"["}
#     for i in s:
#         if i in mapping.values():
#             stack.append(i)
#         elif i in mapping:
#             if not stack or stack[-1]!=mapping[i]:
#                 return False
#             stack.pop()
#         else:
#             return False
#     return not stack
# examples=["()","{()}","[}","(){}[]"]
# for s in examples:
#     print(is_valid(s))
(1, 2, 3, 4)
(1, 2, 4, 3)
(1, 3, 2, 4)
...
(4, 3, 2, 1)
