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
shapes01 = iio.imread(uri="./test/shapes-01.jpg")
print(shapes01.shape) # shape (x, y, 3)
fig, ax = plt.subplots()
# plt.imshow(shapes01)
plt.imsave("loaded-example.jpg", shapes01)

print("making grayscale")
gray_shapes = ski.color.rgb2gray(shapes01)
print(f"Gray Shape: {gray_shapes.shape}")
blurred_shapes = ski.filters.gaussian(gray_shapes, sigma=1.0)
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

print("Applying threshold to image")
threshold = .85 
#too high of a threshold -> background noise
#too low of a threshold -> lose some shapes
binary_mask = blurred_shapes < threshold #creates a new bitmap consisting of only 1s and 0s
plt.imsave("binary_mask.jpg", binary_mask, cmap="gray")