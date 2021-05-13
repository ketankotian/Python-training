def longest():
    words = ['java', 'c++', 'python']
    length = len(words[0])
    max = words[0]
    for i in words:
        if (len(i) > length):
            length = len(i)
            max = i
            print('longest word : ', max, ' length :', length)


longest()


def swap():
    word = 'abcd'
    print(word[-1] + word[-3:-1] + word[-4])


swap()


def reverse():
    msg = 'i learn python'
    print('original :', msg)
    print('reverse :', msg[::-1])


reverse()


def duplicate():
    # remove duplicate from string
    t = ''
    st = 'i learn python'
    for i in st:
        if (i in t):
            pass
        else:
            t = t + i
    print(t)


duplicate()
