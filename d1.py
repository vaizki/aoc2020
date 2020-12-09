import itertools

l = [ int(x) for x in open('i1.txt').read().strip().split('\n') ]
for a,b in itertools.combinations(l, 2):
  if a+b == 2020:
    print(f'{a}*{b}={a*b}')
