import re

bl = open('i7.txt').read().strip().split('\n')
bags = {}
goldy = set()

for b in bl:
  color, cl = b.split(' bags contain', 1)
  if cl == ' no other bags.':
    contents = {}
  else:
    contents = { re.sub(r' bags?', '', x[1]): int(x[0]) for x in [ xx.split(' ',1) for xx in cl[:-1].strip().split(', ') ] }
  bags[color] = contents

# part 1: brute force XMAS
while True:
  glen = len(goldy)
  for color, contents in bags.items():
    if color in goldy:
      continue
    for c,n in contents.items():
      if c == 'shiny gold' or (c in goldy):
        goldy.add(color)
  if len(goldy)==glen:
    break

print('PART1 possible bags:', glen)


# part 2: recurse XMAS

def count_bags(color):
  return sum([ n*count_bags(c) for c,n in bags[color].items()])+1

# remember to subtract 1 for the shiny gold bag itself
print('PART2 bags inside shiny gold bag:', count_bags('shiny gold')-1)
