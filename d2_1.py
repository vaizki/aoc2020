l = open('i2.txt').read().strip().split('\n')
i = 0

for e in l:
  rs, c, s = e.split()
  mm = rs.split('-')
  if (int(mm[0]) <= s.count(c[0]) <= int(mm[1])):
    i += 1

print("Valid passwords:",i)
