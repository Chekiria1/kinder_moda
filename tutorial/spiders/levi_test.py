import re
text = ['\n37                                                    ',
                     '\n38                                                    ',
                     '\n39                                                    ',
                     '\n'
                     '40                                                    ']

'''
c =[]
for b in a:
    b = re.sub(r'\s{1,}$', '', b)
    b = re.sub(r'\n', '', b)
    print('b - {}'.format(b))
    c.append(b)


print(c)'''


'''['21', '22', '23', '24', '25']
sizes = []
s = ''
for size in text:
    size = re.sub(r'\s{1,}$', '', size)
    size = re.sub(r'\n', '', size)
    # print('b - {}'.format(b))
    sizes.append(size)
    s=s+size
text = sizes

print(sizes)
print ('s ---{}'.format(s))'''


def listToString(s):
    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(s))


# Driver code
s = ['21', '22', '23', '24', '25']
print(listToString(s))