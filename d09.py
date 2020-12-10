import itertools

# part 1
nl = list(map(int, open('i09.txt').read().strip().split('\n')))
i = 25

while True:
  combos = list(itertools.combinations(nl[i-25:i], 2))
  sums = list(map(sum, combos))
  if nl[i] not in sums:
    print('INVALID:',nl[i])
    break
  i+=1

# part 2
n = nl[i]
for j in range(0,len(nl)):
  x = nl[j]
  k = j
  while x < n:
    k += 1
    x += nl[k]
  if x == n and k != j:
    cset = nl[j:k+1]
    print('SET:', cset, '\nANSWER2:', min(cset)+max(cset))
