# load adapter ratings into a sorted list
ratings = sorted(map(int, open('i10.txt').read().strip().split('\n')))

# part 1: one run

diffs = [0,0,1]
jolts = 0
for r in ratings:
  diffs[r-jolts-1] += 1
  jolts = r

print('PART1:', diffs[0]*diffs[2])


# part 2: recurse but cache to save a few days...

# preload cache with the highest joltage from part 1
combo_cache = { jolts: 1 }

def paths_to_max(rl):
  if rl[0] in combo_cache:
    return combo_cache[rl[0]]
  path_list = [ rl[i:] for i in (1,2,3) if i < len(rl) and rl[i] <= rl[0]+3 ]
  combos = sum(map(paths_to_max, path_list))
  combo_cache[rl[0]] = combos
  return combos

# finally run all paths from 0 jolts 
print('PART2:', paths_to_max([0]+ratings))

