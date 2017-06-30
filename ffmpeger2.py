import os


DATA = 'data'
VIDEO_DATA = 'video_data'
PEOPLE = ['single', 'double']
BLOCKS = ['base', 'hook', 'in_release', 'in_release_flash',
          'out_release', 'setup_release', 'man_to_man', 'slide_block']
DIRECTIONS = ['front', 'side']
CUT_DIR = 'ct'

# DIRECTION = ['front', 'side']
# PEOPLE = ['single', 'double']

print(DATA)
for person in PEOPLE:
    print('--' + person)

    for block in BLOCKS:
        print('----' + block)

        for direction in DIRECTIONS:
            print('------' + direction)
            in_path0 = VIDEO_DATA + '/' + person + '/' + block + '/' + direction

            if not os.path.exists(in_path0):
                print('ERROR:', in_path0, 'does not exist.')
                continue
            else:
                directories = sorted(os.listdir(in_path0))

                for directory in directories:
                    print('--------' + directory)
                    in_path1 = in_path0 + '/' + directory

                    if not os.path.exists(in_path1):
                        print('ERROR:', in_path1, 'does not exist.')
                        continue
                    else:
                        video = sorted(os.listdir(in_path1))

                        if not video:
                            print('ERROR: video targeted as cut does not exist')
                        else:
                            out_path = DATA + '/' + person + '/' + block + '/' + direction\
                                       + '/' + directory + '/' + CUT_DIR
                            if os.path.exists(out_path):
                                print('ERROR: already exists:', out_path)
                            else:
                                os.makedirs(out_path)
                                command = 'ffmpeg -i %s -ss 0 -r 60 -f image2' % (in_path1 + '/' + video[0])
                                os.system(command + ' ' + out_path + '/' + '%06d.jpg')
