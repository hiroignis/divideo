import os
from PIL import Image


DATA = 'data'
PEOPLE = ['single', 'double']
BLOCKS = ['base', 'hook', 'in_release', 'in_release_flash',
          'out_release', 'setup_release', 'man_to_man', 'slide_block']
DIRECTIONS = ['front', 'side']
CROP_DIR = 'cr00'
CUT_DIR = 'ct'
CROP_AREA = (520, 223, 520 + 800, 223 + 800)

# DIRECTION = ['front', 'side', varti]
# PEOPLE = ['single', 'double']

print(DATA)
for person in PEOPLE:
    print('--' + person)

    for block in BLOCKS:
        print('----' + block)

        for direction in DIRECTIONS:
            print('------' + direction)
            in_path0 = DATA + '/' + person + '/' + block + '/' + direction

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
                        data_directories = sorted(os.listdir(in_path1))

                        if not CUT_DIR in data_directories:
                            print('ERROR: ', )
                        else:
                            in_path2 = in_path1 + '/' + CUT_DIR

                            out_path = in_path1 + '/' + CROP_DIR
                            if os.path.exists(out_path):
                                print('ERROR: already exist:', out_path)
                                continue
                            else:
                                os.mkdir(out_path)

                                if not os.path.exists(in_path2):
                                    print('ERROR:', in_path2, 'does not exist.')
                                    continue
                                else:
                                    images = sorted(os.listdir(in_path2))

                                    for image in images:
                                        if image:
                                            # print('----------' + image)
                                            in_image = Image.open(in_path2 + '/' + image)
                                            out_image = in_image.crop(CROP_AREA)
                                            image_name = in_image.filename.split('/')[-1]
                                            out_image.save(out_path + '/' + image_name)
                                            in_image.close()
                                            out_image.close()
