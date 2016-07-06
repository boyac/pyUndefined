# Red envelope lucky draw
# ref: https://en.wikipedia.org/wiki/WeChat_red_envelope
"""
The user assigns a lump sum to a group red envelope, 
and the number of small red envelopes within it. 
After posting to a group chat, WeChat will randomly assign the amount in each envelope to each recipient
"""

import numpy as np, numpy.random
def money(amount, n):
    hong_bao = np.random.dirichlet(np.ones(n),size=1) * amount
    np.set_printoptions(precision=2)
    return hong_bao
print money(10, 15) #假設把10元，隨機分給15人。
