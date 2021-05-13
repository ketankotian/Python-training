# 1. counting even & odd
num = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0
for i in num:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print('even:', even)
print('odd:', odd)

# 2. unique elements in list
numb = [1, 2, 3, 4, 5, 1, 2, 1, 2]
uni = []
for i in numb:
    if i not in uni:
        uni.append(i)
print('original :', numb, '; unique item :', uni)

# 3. multiply number with list
nums = [2, 4, 6, 9, 11]
n = 2
new = list(map(lambda number: number * n, nums))
print('original :', nums, ' result:', ', '.join(map(str, new)))

# 4. count upper & lower case
msg = 'The Quick Brown Fox'
upper = 0
lower = 0
for i in msg:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
print('uppercase:', upper)
print('lowercase:', lower)
