# string="abcdefghijklmnopqrstuvwxyz"
# width=5
# def function(str,max_width):
#     for i in range(0,len(str),max_width):
#         print (str[i:i+max_width])
    
# function(string,width)

# string="aaabbc"
# count=0
# n=string[0]
# res=""
# for i in range(0,len(string)):
#     if string[i]==n:
#         count+=1
#     else:
#         res+=n+str(count)
#         n=string[i]
#         count=1
# res+=n+str(count)
# print(res)

#second max
# list=[1,2,3,4,5,6,7,8]
# max=list[0]
# max2=list[1]
# for i in range(0,len(list)):
#     if list[i]>max and list[i]>max2:
#         max2=max
#         max=list[i]

#     if max<list[i]>max2:
#         max2=list[i]
# print(max2)

# string="5udaya sree final"
# s2=string.split(" ")
# final=""
# for i in s2:
#     res=""
#     if i[0].isalpha():
#         res=i[0].upper()
#         res+=i[1::]
#     else:
#         res+=i
#     final+=res+" "
# # print(final.strip())
# print(final.strip())
# l=[1,2,3]
# l2=[1,1,1]
# def compare(a,b):
#     count_a=0
#     count_b=0
#     for i in range(len(a)):
        
        
#         if a[i]>b[i]:
#             count_a+=1
#         elif a[i]<b[i]:
#             count_b+=1

#     return(count_a,count_b)
# print(compare([1,1,2],[2,3,4,5,6,1]))


# def compare_lists(a, b):
#     score_a = 0
#     score_b = 0

#     for i in range(len(a)):
#         if a[i] > b[i]:
#             score_a += 1
#         elif a[i] < b[i]:
#             score_b += 1
#         # if equal, no points

#     return [score_a, score_b]

# # Test
# a = [1, 2, 3]
# b = [1, 2, 1]
# print(compare_lists(a, b))


# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     return fact
# print(factorial(5))
# print(factorial(7))

# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))

# def factorial(n,i=1):
#     if i>n:
#         return 
#     else:
#         return n*factorial(n+1)
# print(factorial(5))

#using method
# string="udayasree"
# for i in range(0,len(string)):
#     if string.count(string[i])==1:
#         print(string[i])
#         break


#without using methods
# string="hello world"
# res=""
# string2=[]
# for i in string:
#     if i not in string2:
#         string2.append(i)
# print(string2[0])


# list1=[1,2,3,4]
# list2=[2,1,4,3]
# def function(a,b):
#     count_a=0
#     count_b=0
#     for i in range(len(a)):
#         if a[i]>b[i]:
#             count_a+=1
#         if a[i]<b[i]:
#             count_b+=1
#     return [count_a,count_b]
# print(function(list1,list2))

# list=[529,320,654,128,546]
# for i in range(len(list)):
#     for j in range(0,len(list)-i-1):
        
#         if list[j] > list[j+1]:
#             list[j],list[j+1]=list[j+1],list[j]
# print(list)

# list=[1,2,3,4,5,6]
# n=len(list)
# for i in range(n//2):
#     list[i],list[n-1-i]=list[n-1-i],list[i]
# print(list)

# string="madam"
# for i in range(len(string)):
#     if string[i]==string[len(string)-1-i]:
#         pass
# print("palindrome")

# list=[1,2,3,4,8,5,7,6,13]
# for i in range(len(list)-1):
#     if list[i]>list[i+1]:
#         list[i],list[i+1]=list[i+1],list[i]
# print("max2: ", list[len(list)-2])


# def exist(board,word):
#     rows=len(board)
#     cols=len(board[0])
#     def dfs (r,c,i):
#         if i==len(word):
#             return True
#         if r<0 or c<0 or r>=rows or c>=cols:
#             return False
#         if board[r][c]!=word[i]:
#             return False
#         temp=board[r][c]
#         board[r][c]="#"
         
#         found=(
#             dfs (r+1, c, i+1) or
#             dfs (r-1, c, i+1) or
#             dfs (r, c+1, i+1) or
#             dfs (r, c-1, i+1) 

#         )
#         board[r][c]=temp
#         return found
#     for i in range(rows):
#         for j in range(cols):
#             if dfs(i,j,0):
#                 return True
#     return False
# board=[["a","b","c","e"],
#        ["s","f","c","s"],
#        ["a","d","e","e"]
#        ]

# word1="abcced"
# word2="see"
# word3="abab"
# print(exist(board,word1))
# print(exist(board,word2))
# print(exist(board,word3))



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
#         found=(
#             dfs(r+1,c,i+1) or
#             dfs(r-1,c,i+1) or
#             dfs(r,c+1,i+1) or
#             dfs(r,c-1, i+1)
#         )
#         board[r][c]=temp
#         return found
#     for i in range(rows):
#         for j in range(cols):
#             if dfs(i,j,0):
#                 return True
#     return False
# board=[["a","b","c","e"],
#     ["s","f","c","s"],
#     ["a","d","e","e"]
#     ]

# word1="abcced"
# word2="see"
# word3="abab"

# print(exist(board,word1))
# print(exist(board,word2))
# print(exist(board,word3))
            

# string = input("enter the string: ")
# dict = {}
# for char in string:
#     if char in dict:
#         dict[char] += 1
#     else:
#         dict[char] = 1
# max_char =""
# max_count = 0
# for char in dict:
#     if dict[char] > max_count:
#         max_count = dict[char]
#         max_char = char
# print( max_char, max_count)

# list=[1,2,3,4,6,7,8]
# list_sum=0
# n=len(list)+1
# for i in range(len(list)):
#     list_sum+=list[i]
#     sum=(n*(n+1))//2
#     miss=sum-list_sum
# print(miss)


# s = "hello"
# dict={}
# for ch in set(s):
#     dict[ch]=s.count(ch)
# print(dict)


# 2. First missing positive number
lst = [3, 4, -1, 1]
nums = set(lst)
for i in range(1, len(lst) + 2):
    if i not in nums:
        print("First missing positive:", i)
        break


