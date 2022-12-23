with open('input1.txt', 'r') as f:
    input_data = f.readlines()

best = [0, 0, 0]
curr = 0
for item in input_data:
    if item == '\n':
        if curr > best[2]:
            best[0] = best[1]
            best[1] = best[2]
            best[2] = curr
        elif curr > best[1]:
            best[0] = best[1]
            best[1] = curr
        elif curr > best[0]:
            best[0] = curr

        curr = 0
        continue
    else:
        num = int(item)
        curr += num

print(sum(best))