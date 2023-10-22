import glob

import imageio.v3 as iio 
#pip install imageio
import ipympl
#pip install ipympl
import matplotlib
import matplotlib.pyplot as plt
#pip install matplotlib
import numpy as np
#pip install numpy
import skimage as ski
#pip install scikit-image

## Make WSL work
matplotlib.use("Agg")

print("Loading the image")
shapes01 = iio.imread(uri="./images/snappedImage4.bmp")
print(shapes01.shape) #already black and white, no need to make gray
fig, ax = plt.subplots()
# plt.imshow(shapes01)
# plt.imsave("loadedimage.jpg", shapes01)
# should just be gray, no difference

print("making grayscale")
# gray_shapes = ski.color.rgb2gray(shapes01)
blurred_shapes = ski.filters.gaussian(shapes01, sigma=1.0)
fig, ax = plt.subplots()
# plt.imshow(blurred_shapes, cmap="gray")
plt.imsave("blurredimage.jpg", blurred_shapes, cmap="gray")

print("making histogram")
histogram, bin_edges = np.histogram(blurred_shapes, bins=256, range=(0.0, 1.0))

fig,ax = plt.subplots()
plt.plot(bin_edges[0:-1], histogram)
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.xlabel("pixels")
plt.xlim(0, 1.0)
plt.savefig("histogram.jpg")

print("making masked image")
threshold = .3
#.1 too low, need to include more
#.2 a bit too low
#.3 shows the part, background weak tho
binary_mask = blurred_shapes < threshold
plt.imsave("binary_mask.jpg", binary_mask, cmap="gray")