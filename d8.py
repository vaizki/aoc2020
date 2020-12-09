import copy

oprog = [ x.split() for x in open('i8.txt').read().strip().split('\n') ]

def run(prog):
  ip = 0 
  acc = 0
  visited = set()
  while True:
    if ip == len(prog)-1:
      return (True, acc)
    if ip in visited:
      return (False, acc)
    visited.add(ip)
    instr, param = prog[ip]
    if instr == 'acc':
      acc += int(param)
      ip += 1
    if instr == 'jmp':
      ip += int(param)
    if instr == 'nop':
      ip += 1
      continue

# part 1
res, acc = run(oprog)
print('PART1:', acc)

# part 2
for mp in range(0,len(oprog)):
  prog = copy.deepcopy(oprog)
  if prog[mp][0] == 'jmp':
    prog[mp][0] = 'nop'
  elif prog[mp][0] == 'nop':
    prog[mp][0] = 'jmp'
  res, acc = run(prog)
  if res:
    print('PART2:', acc)
    break
