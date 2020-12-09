import re

def val_height(x):
  unit = x[-2:]
  val = int(x[:-2])
  if unit == 'cm' and 150 <= val <= 193:
    return True
  if unit == 'in' and 59 <= val <= 76:
    return True
  return False
  

VALID = { 'byr': lambda x: (1920 <= int(x) <= 2002),
	'iyr': lambda x: (2010 <= int(x) <= 2020),
	'eyr': lambda x: (2020 <= int(x) <= 2030),
	'hgt': val_height,
	'hcl': lambda x: re.match(r'^#[0-9a-f]{6}$', x),
	'ecl': lambda x: x in ('amb','blu','brn','gry','grn','hzl','oth'),
	'pid': lambda x: re.match(r'^[0-9]{9}$', x)
	}

pl = [ l.strip() for l in open('i4.txt').read().split('\n\n') ]
valid = 0

for pp in pl:
  fields = { x.split(':')[0]: x.split(':')[1] for x in pp.split() }
  for fn,fv in VALID.items():
    if fn not in fields or not fv(fields[fn]):
      break
  else:
    valid += 1

print('Valid:',valid)
