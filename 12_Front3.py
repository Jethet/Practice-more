#Given a string, the front is first 3 chars. If string length less
# than 3, front is whatever is there. Return new string which is
# 3 copies of the front.

def front3(str):
    if len(str) > 3:
        str = str[0:3] * 3
        return str
    else:
        return str * 3

print(front3('chocolate'))
print(front3('ab'))
