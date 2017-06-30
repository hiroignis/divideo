import os


START_TEXT = 'start_single.txt'
TRAIN_TEXT = 'train_single.txt'

# DIRECTION = ['front', 'side', varti]
# PEOPLE = ['single', 'double']

B_BASE = 0
B_HOOK = 1
B_IN_RELEASE = 2
B_IN_RELEASE_FLASH = 3
B_OUT_RELEASE = 4
B_SETUP_RELEASE = 5
B_MAN_TO_MAN = 6
B_SLIDE_BLOCK = 7


def tag_set(block_name):
    if block_name == 'base':
        return B_BASE
    elif block_name == 'hook':
        return B_HOOK
    elif block_name == 'in_release':
        return B_IN_RELEASE
    elif block_name == 'in_release_flash':
        return B_IN_RELEASE_FLASH
    elif block_name == 'out_release':
        return B_OUT_RELEASE
    elif block_name == 'setup_release':
        return B_SETUP_RELEASE
    elif block_name == 'man_to_man':
        return B_MAN_TO_MAN
    elif block_name == 'slide_block':
        return B_SLIDE_BLOCK

    print('ERROR: no such block name:', block_name)
    return -1


with open(START_TEXT, 'rt') as fin:
    with open(TRAIN_TEXT, 'wt') as fout:
        line = fin.readline()

        while line:
            line = line.split(' ')
            tag = tag_set(line[0].split('/')[2])
            fout.write(line[0] + ' ' + line[1][0:-1] + ' ' + str(tag) + '\n')
            print(line[0] + ' ' + line[1][0:-1] + ' ' + str(tag) + '\n')
            line = fin.readline()
