

import collections
denderqueue = collections.deque(['april','may','june'])
denderqueue.append('july')
denderqueue.append('august')
print(denderqueue)
denderqueue.appendleft('march')
denderqueue.appendleft('february')
print(denderqueue)
denderqueue.pop()
print(denderqueue)
denderqueue.popleft()
print(denderqueue)
