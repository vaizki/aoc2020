# skip first row
rows = open('i03.txt').read().strip().split('\n')[1:]
x = 0
trees = 0
for r in rows:
  x = (x+3) % len(r)
  if r[x] == '#':
    trees += 1
print('TREES:',trees)
