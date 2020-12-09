l = open('i2.txt').read().strip().split('\n')
i = 0

for e in l:
  rs, c, s = e.split()
  mm = rs.split('-')
  c = c[0]
  s1 = s[int(mm[0])-1]
  s2 = s[int(mm[1])-1]
  if ((s1 == c or s2 == c) and not (s1==s2)):
    i += 1

print("Valid passwords:",i)

