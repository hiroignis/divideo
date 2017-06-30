import os


DATA = 'data'
PEOPLE = ['single']
BLOCKS = {'base', 'hook', 'in_release', 'in_release_flash',
          'out_release', 'setup_release', 'man_to_man', 'slide_block'}
DIRECTIONS = ['front']
CROP_DIR = 'cr00'
CUT_DIR = 'ct'
TARGET = CROP_DIR

TRAIN_TEXT = 'train.txt'

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


with open(TRAIN_TEXT, 'wt') as f:
    print('' + DATA)

    for person in PEOPLE:
        print('--' + person)

        for block in BLOCKS:
            print('----' + block)
            tag = tag_set(block)

            for direction in DIRECTIONS:
                print('------' + direction)
                in_path0 = DATA + '/' + person + '/' + block + '/' + direction

                if not os.path.exists(in_path0):
                    print('ERROR:', in_path0, 'does not exists.')
                    continue
                else:
                    directories = sorted(os.listdir(in_path0))

                    for directory in directories:
                        print('--------' + directory)
                        in_path1 = in_path0 + '/' + directory + '/' + TARGET

                        if not os.path.exists(in_path1):
                            print('ERROR:', in_path1, 'does not exists.')
                            continue
                        else:
                            images = sorted(os.listdir(in_path1))

                            for image in images:
                                f.write(in_path1 + '/' + image + ' ' + str(tag) + '\n')
                                # print(in_path1 + '/' + image + ' ' + str(tag))
