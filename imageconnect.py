import os
from PIL import Image

BLOCK = 'in_release_flash'

os.mkdir('./pred')
# 840x840
images_list = os.listdir('./' + BLOCK + '/sample/')
images_list.sort()

# 800x600
graph_list = os.listdir('./' + BLOCK + '/bargraph2/')
graph_list.sort()

# 800x600
dum_jpg = Image.open('dum.jpg', 'r')

for i, image in enumerate(images_list):
    image = Image.open('./' + BLOCK + '/sample/' + image)
    canvas = Image.new('RGB', (1640, 840), (255, 255, 255))

    canvas.paste(image, (0, 0))

    if 0 <= i < 60:
        dum = Image.open('dum.jpg', 'r')
        dum = dum.point(lambda x: x * (1 / 240 * i + 0.75))
        air = Image.new('RGB', (800, 600), (255, 255, 255))
        air = air.point(lambda x: x * (1 / 240 * i + 0.75))
        canvas.paste(air, (840, 0))
        canvas.paste(dum, (840, 240))
        air.close()
        dum.close()
    elif 60 <= i < 120:
        graph = Image.open('./' + BLOCK + '/bargraph2/' + graph_list[i - 60])
        canvas.paste(graph, (840, 240))
        graph.close()
    elif 120 <= i < 180:
        graph = Image.open('./' + BLOCK + '/bargraph2/' + graph_list[-1])
        graph = graph.point(lambda x: x * (-1 / 240 * i + 1.5))
        air = Image.new('RGB', (800, 600), (255, 255, 255))
        air = air.point(lambda x: x * (-1 / 240 * i + 1.5))
        canvas.paste(air, (840, 0))
        canvas.paste(graph, (840, 240))
        air.close()
        graph.close()
    else:
        break

    """
    if 0 <= i < 60:
        dum = Image.open('dum.jpg', 'r')
        dum = dum.point(lambda x: x * (1 / 240 * i + 0.75))
        air = Image.new('RGB', (800, 600), (255, 255, 255))
        air = air.point(lambda x: x * (1 / 240 * i + 0.75))
        canvas.paste(air, (840, 0))
        canvas.paste(dum, (840, 240))
        air.close()
        dum.close()
    elif 60 <= i < 140:
        graph = Image.open('./' + BLOCK + '/bargraph1/' + graph_list[i - 60])
        canvas.paste(graph, (840, 240))
        graph.close()
    elif 140 <= i < 180:
        graph = Image.open('./' + BLOCK + '/bargraph1/' + graph_list[-1])
        graph = graph.point(lambda x: x * (-1 / 160 * i + 15 / 8))
        air = Image.new('RGB', (800, 600), (255, 255, 255))
        air = air.point(lambda x: x * (-1 / 160 * i + 15 / 8))
        canvas.paste(air, (840, 0))
        canvas.paste(graph, (840, 240))
        air.close()
        graph.close()
    else:
        break
    """

    canvas.save('./pred/%06d.jpg' % i, 'JPEG', quality=100, optimize=True)
