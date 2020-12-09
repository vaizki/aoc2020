prog = [ x.split() for x in open('i8.txt').read().strip().split('\n') ]
ip = 0 
acc = 0
visited = set()

while True:
  if ip in visited:
    print(f'ip={ip},acc={acc}')
    break
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
