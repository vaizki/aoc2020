grps = [ x.strip() for x in open('i06.txt').read().split('\n\n') ]
tot1 = 0
tot2 = 0

for g in grps:
  ans = [ set(x) for x in g.split() ]
  tot1 += len(set.union(*ans))
  tot2 += len(set.intersection(*ans))

print("ANSWERS:", tot1, tot2)
