# 1. second largest
from collections import Counter

num = [100, 70, 10, 45]
num.sort()
print(num)
print('largest :', num[-1])  # use [0] to find smallest and [1] to find second smallest
print('second largest :', num[-2])

# alternate
max1 = max(num)  # use min() to find smallest and follow same process
print('largest :', max1)
num.remove(max1)
smax = max(num)
print('second largest :', smax)


# 2.common from 2list
def common(a, b):
    op = False
    for x in a:
        for y in b:
            if x == y:
                op = True
                print(op)


a = [1, 2, 3, 4]
b = [5, 6, 4, 7]
common(a, b)

# 3.frequency of a number
list1 = [1, 2, 3, 4, 5, 6, 5, 1, 5, 4, 5]
freq = Counter(list1)
print(freq)

#alternate
fre={}
for i in list1:
    if i in fre:
        fre[i]=fre[i]+1
    else:
        fre[i]=1
print('frequency :',fre)

# 4. unique values in list
numb = [1, 2, 3, 4, 5, 1, 2, 6, 1, 2]
uni = []
a = 0
for i in numb:
    if i not in uni:
        a += 1
        uni.append(i)
print('unique item :', uni, ' & count :', a)

# alternate
un = Counter(numb).keys()
print('unique item :', un, ' & count :', len(un))
