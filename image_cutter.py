import os
from PIL import Image


DATA = 'data'
PEOPLE = ['single']
BLOCKS = ['base', 'hook', 'in_release', 'in_release_flash',
          'out_release', 'setup_release', 'man_to_man', 'slide_block']
DIRECTIONS = ['front']
CROP_AREA = (662, 286, 662 + 640, 286 + 640)
CROP_DIR = 'cr00'
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

                if CUT_DIR in os.listdir():
                    images = sorted(os.listdir(CUT_DIR))
                    os.mkdir(CROP_DIR)
                else:
                    continue

                for image in images:
                    if image:
                        print('-----' + image)
                        in_image = Image.open(CUT_DIR + '/' + image)
                        out_image = in_image.crop(CROP_AREA)
                        out_image.save(CROP_DIR + '/' + in_image.filename)
                        in_image.close()
                        out_image.close()

                os.chdir('../')
            os.chdir('../')
        os.chdir('../')
    os.chdir('../')
os.chdir('../')
