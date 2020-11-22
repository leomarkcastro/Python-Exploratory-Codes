import collections

name = {"alex", "marry ann"}

de = collections.deque(name)

de.append("leo")

de.appendleft("ben")

print(de)