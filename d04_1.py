REQ = ('byr','iyr','eyr','hgt','hcl','ecl','pid')
pl = [ l.strip() for l in open('i04.txt').read().split('\n\n') ]
valid = 0

for pp in pl:
  fields = [ x.split(':')[0] for x in pp.split() ]
  for fn in REQ:
    if fn not in fields:
      break
  else:
    valid += 1
print('Valid:',valid)
