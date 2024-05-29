import imageio.v3 as iio

image_files = ['team-pic1.png','team-pic2.png']

images = []

for image_file in image_files:
    images.append(iio.imread(image_file))

iio.imwrite('team.gif', images, duration=500, loop=0)
