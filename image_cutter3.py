import os
from PIL import Image


ROOT = '/media/ignis/IGNIS_BLACK/IIIIGNIS/'

DIRECTION = 'side'
CROP_DIR = 'sample'
CUT_DIR = 'ct'
START_TEXT = '/home/ignis/IGNIS/PycharmProjects/otmove/text/humans/single_test/double_6classSHIOMI_base3.txt'
CROP_AREA = (500, 203, 500 + 840, 203 + 840)


with open(START_TEXT, 'rt') as fin:
    read_line = fin.readline()

    while read_line:
        print(read_line[:-2])
        path = ROOT + read_line.split(' ')[0]
        start = read_line.split(' ')[1]

        if start is '':
            print('SYSTEM: skip', path)
            read_line = fin.readline()
            continue
        else:
            read_path = path.split('/')
            read_path[8] = DIRECTION
            direction_line = '/'.join(element for element in read_path) + '/'

            if not os.path.exists(path + CUT_DIR):
                print('ERROR: ' + direction_line + CUT_DIR + ' does not exist.')
                read_line = fin.readline()
                continue
            elif not os.path.exists(direction_line + CROP_DIR):
                print('SYSTEM: create ' + CROP_DIR)
                os.mkdir(direction_line + CROP_DIR)

                images = sorted(os.listdir(direction_line + CUT_DIR))

                for image in images:
                    if image:
                        if int(start) - 60 < int(image.split('.')[0]) < int(start) + 180:
                            in_image = Image.open(direction_line + CUT_DIR + '/' + image)
                            out_image = in_image.crop(CROP_AREA)
                            image_name = in_image.filename.split('/')[-1]
                            out_image.save(direction_line + CROP_DIR + '/' + image_name)
                            in_image.close()
                            out_image.close()

        read_line = fin.readline()
