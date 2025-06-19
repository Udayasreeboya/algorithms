# def is_valid(s):
#     stack=[]
#     mapping={"]":"[",")":"(","}":"{"}
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
# test_cases = [
#         "()",       # True
#         "()[]{}",   # True
#         "(]",       # False
#         "([])",     # True
#         "([)]",     # False
#         "{[]}",     # True
#         "",         # True (empty string is valid)
#         "[",        # False
#         "]",        # False
#     ]

# for s in test_cases:
#     print(f"Input: {s} => Output: {is_valid(s)}")

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
# check=["()","{}","[}","({[]})"]
# for s in check:
#     print(is_valid(s))
            
string="this is udayasree from anantapuram"
list=string.split(" ")
min=""
for i in list:
  
    if len(min)<len(i):
        min=i
print(min)
        



        