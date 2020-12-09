# skip first row
rows = open('i3.txt').read().strip().split('\n')[1:]
tulo = 1
combos = ((1,1),(3,1),(5,1),(7,1),(1,2))
for right,down in combos:
  rc = 0
  trees = 0
  x = 0
  for r in rows:
    rc += 1
    if (rc % down):
      continue
    x = (x+right) % len(r)
    if r[x] == '#':
      trees += 1
  print(right, down, 'hits:', trees)
  tulo *= trees
print('Answer:', tulo)
