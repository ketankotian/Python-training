# 1. map two lists into a dictionary
from collections import defaultdict, Counter

list1 = ['dont', 'let', 'me', 'down']
list2 = [1, 2, 3, True]
new = dict(zip(list1, list2))
print(type(new), '->', new)

# 2. Group Similar items to Dictionary Values List
num = [1, 2, 3, 1, 2, 3, 1, 2, 3, 2, 5, 2, 5]
op = defaultdict(list)
for i in num:
    op[i].append(i)
print(dict(op))

#alternate :1
print(Counter(num))
#alternate :2
r={k:[k]*v for k,v in Counter(num).items()}
print(r)

# 3. convert a tuple to a string
tup = ('hi', 'hello', 'world')
st = ''.join(tup)  # ''.join(tup) =
print(st)

# 4. update the list values in the dictionary
dit = {
    'name': 'coldplay',
    'gener': ['pop', 'rock']
}
a = ['hiphop', 'jazz']
dit['gener'] = dit['gener'] + a
print(dit)
