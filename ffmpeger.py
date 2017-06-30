import os


DATA = 'data'
PEOPLE = ['single']
BLOCKS = ['base', 'hook', 'in_release', 'in_release_flash',
          'setup_release', 'out_release', 'man_to_man', 'slide_block']
DIRECTIONS = ['front']
CUT_DIR = 'ct'

# DIRECTION = ['front', 'side']
# PEOPLE = ['single', 'double']


os.chdir(DATA)
for person in PEOPLE:
    print('-' + person)
    os.chdir(person)

    for block in BLOCKS:
        print('--' + block)
        os.chdir(block)

        for direction in DIRECTIONS:
            print('---' + direction)
            os.chdir(direction)
            directories = sorted(os.listdir())

            for directory in directories:
                print('----' + directory)
                os.chdir(directory)
                video = os.listdir()
                if video:
                    os.mkdir(CUT_DIR)
                    command = 'ffmpeg -i %s -ss 0 -r 60 -f image2' % video[0]
                    os.system(command + ' ' + CUT_DIR + '/' + '%06d.jpg')

                os.chdir('../')
            os.chdir('../')
        os.chdir('../')
    os.chdir('../')
os.chdir('../')
