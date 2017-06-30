import os
from PIL import Image


images_list = list()

images_list.append(os.listdir('./base/sample/'))
images_list.append(os.listdir('./hook/sample/'))
images_list.append(os.listdir('./in_release/sample/'))
images_list.append(os.listdir('./man_to_man/sample/'))
images_list.append(os.listdir('./out_release/sample/'))
images_list.append(os.listdir('./slide_block/sample/'))

for images in images_list:
    images.sort()

os.mkdir('./6class')

for num, (b, h, i, m, o, s) in enumerate(zip(images_list[0], images_list[1], images_list[2], images_list[3], images_list[4], images_list[5])):
    image_b = Image.open('./base/sample/' + b)
    image_h = Image.open('./hook/sample/' + h)
    image_i = Image.open('./in_release/sample/' + i)
    image_m = Image.open('./man_to_man/sample/' + m)
    image_o = Image.open('./out_release/sample/' + o)
    image_s = Image.open('./slide_block/sample/' + s)

    image_b = image_b.resize((420, 420))
    image_h = image_h.resize((420, 420))
    image_i = image_i.resize((420, 420))
    image_m = image_m.resize((420, 420))
    image_o = image_o.resize((420, 420))
    image_s = image_s.resize((420, 420))

    canvas = Image.new('RGB', (1260 + 10, 840 + 5), (0, 0, 0))

    canvas.paste(image_b, (0, 0))
    canvas.paste(image_h, (420 + 5, 0))
    canvas.paste(image_i, (840 + 5 + 5, 0))
    canvas.paste(image_m, (0, 420 + 5))
    canvas.paste(image_o, (420 + 5, 420 + 5))
    canvas.paste(image_s, (840 + 5 + 5, 420 + 5))

    canvas.save('./6class/%06d.jpg' % num, 'JPEG', quality=100, optimize=True)
