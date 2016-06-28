import random

P = 3000
ATR = 45
A = ATR*2


def sequence(length=99):
   
    rtn = []
    p = P
    r = range(length)
    for m in r: 
        
        p += random.randint(-1*A, A)
        rtn.append(p)

    return rtn

#s = sequence()
#print s
# the  probability of one_side + not_zhisun is almost 1

def one_side(runtime=9999, scope=1.1):
    cnt = 0
    r = range(runtime)
    for n in r:
        s = sequence()
        if max(s) >= P*scope:
            cnt += 1
    return cnt / float(runtime)


#print one_side(scope=1.02)
#print one_side(scope=1.04)


def not_zhisun(runtime=9999, scope=0.95):
    cnt = 0
    for n in range(runtime):
        s = sequence()
        if min(s) > P*scope:
            cnt += 1
    return cnt / float(runtime)

#print not_zhisun(scope=0.98)
#print not_zhisun(scope=0.96)


def lowwest_between_1atr_2atr(runtime=9999):
    cnt = 0
    for n in range(runtime):
        s = sequence()
        if P - 2*ATR < min(s) < P - 1*ATR:
            cnt += 1

    #print cnt
    return cnt / float(runtime)

def min_higher(runtime=9999):
    cnt = 0
    for n in range(runtime):
        s = sequence()
        if min(s) > P - 7*ATR:
            cnt += 1

    #print cnt
    return cnt / float(runtime)

print lowwest_between_1atr_2atr()
print min_higher()