# quick and dirty code to generate queens

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("num")
args = parser.parse_args()
num = int(args.num)

# each row has value
for i in range(num):
    print('(or ', end='')
    for j in range(num):
        print(f'Q{i}{j} ', end='')
    print(')')

# each col has value
for i in range(num):
    print('(or ', end='')
    for j in range(num):
        print(f'Q{j}{i} ', end='')
    print(')')

# not in same row
for i in range(num):
    for j in range(num):
        print(f'(implies Q{i}{j} (and ', end='')
        for k in range(num):
            if j != k:
                print(f'(not Q{i}{k})', end='')
        print('))')


# not in same col
for i in range(num):
    for j in range(num):
        print(f'(implies Q{i}{j} (and ', end='')
        for k in range(num):
            if i != k:
                print(f'(not Q{k}{j})', end='')
        print('))')


# diagonals
for i in range(num):
    for j in range(num):
        # up left
        i2, j2 = i-1, j-1
        num_added = 0
        curr_str = f'(implies  Q{i}{j} (and '
        while i2 >= 0 and j2 >= 0:
            curr_str += f'(not Q{i2}{j2}) '
            i2 -= 1
            j2 -= 1
            num_added += 1
        curr_str += '))'
        if num_added > 0:
            if num_added == 1:
                curr_str = curr_str.replace(' (and', '')
                curr_str = curr_str.replace('))', ')')
            print(curr_str)

        # up right
        i2, j2 = i-1, j+1
        num_added = 0
        curr_str = f'(implies  Q{i}{j} (and '
        while i2 >= 0 and j2 < num:
            curr_str += f'(not Q{i2}{j2}) '
            i2 -= 1
            j2 += 1
            num_added += 1
        curr_str += '))'
        if num_added > 0:
            if num_added == 1:
                curr_str = curr_str.replace(' (and', '')
                curr_str = curr_str.replace('))', ')')
            print(curr_str)

        # down left
        i2, j2 = i+1, j-1
        num_added = 0
        curr_str = f'(implies  Q{i}{j} (and '
        while i2 < num and j2 >= 0:
            curr_str += f'(not Q{i2}{j2}) '
            i2 += 1
            j2 -= 1
            num_added += 1
        curr_str += '))'
        if num_added > 0:
            if num_added == 1:
                curr_str = curr_str.replace(' (and', '')
                curr_str = curr_str.replace('))', ')')
            print(curr_str)

        # down right
        i2, j2 = i+1, j+1
        num_added = 0
        curr_str = f'(implies  Q{i}{j} (and '
        while i2 < num and j2 < num:
            curr_str += f'(not Q{i2}{j2}) '
            i2 += 1
            j2 += 1
            num_added += 1
        curr_str += '))'
        if num_added > 0:
            if num_added == 1:
                curr_str = curr_str.replace(' (and', '')
                curr_str = curr_str.replace('))', ')')
            print(curr_str)
