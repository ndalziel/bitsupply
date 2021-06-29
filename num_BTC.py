import math

def num_BTC(b):
    tokens = 0
    reward = 50
    for i in range (1,b+1):
        if i % 210000 == 0:
            reward = reward / 2
        tokens = tokens + reward
    return tokens

#print (num_BTC(210000))