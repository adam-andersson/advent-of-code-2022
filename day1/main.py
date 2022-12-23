with open('input1.txt', 'r') as f:
    input_data = f.readlines()

best = 0
curr = 0
for item in input_data:
    if item == '\n':
        curr = 0
        continue
    else:
        num = int(item)
        curr += num

    if curr > best:
        best = curr

print(best)