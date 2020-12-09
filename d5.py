bl = open('i5.txt').read().strip().split('\n')
max_seat = 0
occupied = set()

def find(min, max, s, upc):
  if len(s) == 1:
    return max if s == upc else min
  if s.startswith(upc):
    return find(min+int((max-min)/2)+1, max, s[1:], upc)
  else:
    return find(min, max-int((max-min)/2)-1, s[1:], upc)

for bp in bl:
  row, pos = bp[:7], bp[7:]
  r = find(0,127,row,'B')
  p = find(0,7,pos,'R')
  seat_id = r*8+p
  occupied.add(seat_id)
  if seat_id > max_seat:
    max_seat = seat_id

print('MAX SEAT:', max_seat)

last = 0
for seat in sorted(occupied):
  if last and seat > last+1:
    print('MY SEAT:', seat-1)
  last = seat
