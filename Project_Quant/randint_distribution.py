# check the distribution of each number of randomly rolling dice

from collections import Counter
import random

n = 100000
c = Counter(random.randint(1, 6) for _ in xrange(n))
for i in range(1,7):
    print '%2s  %02.10f%%' % (i, c[i] * 100.0 / n)
