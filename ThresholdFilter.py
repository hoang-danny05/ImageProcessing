# import glob

import imageio.v3 as iio 
#pip install imageio
# import ipympl
#pip install ipympl
# import matplotlib
import matplotlib.pyplot as plt
#pip install matplotlib
import numpy as np
#pip install numpy
import skimage as ski
#pip install scikit-image

## Make WSL work
# matplotlib.use("Agg")

class ThresholdFilter:
    def __init__(self, imagePath="./images/snappedImage4.bmp", inputType="Grayscale"):
        self.imagePath = imagePath
        if (inputType == "Grayscale") or (inputType == "Color"):
            self.inputType = inputType #Grayscale or Color
        else:
            raise ValueError(f"Invalid input type of {inputType}")

                 
    def loadImage(self):
        print("Loading image")
        if (self.inputType == "Color"):
            self.image = iio.imread(uri=self.imagePath)
            # plt.imshow(self.image)
        elif (self.inputType == "Grayscale"):
            self.gray_image = iio.imread(uri=self.imagePath)
            # plt.imshow(self.gray_image, cmap="gray")
        else:
            raise ValueError(f"Invalid input type of {self.inputType}")
        # print(f"Image loaded with shape {self.image.size}")

    def blurImage(self):
        if self.inputType == "Color":
            self.gray_image = ski.color.rgb2gray(self.image)
        self.blurred_image = ski.filters.gaussian(self.gray_image, sigma=1.0)
        # fig, ax = plt.subplots()
        # plt.imshow(self.blurred_image, cmap="gray")
        # plt.imsave("./out/blurredimage.jpg", blurred_shapes, cmap="gray")

    def createHistogram(self):
        print("making histogram")
        histogram, bin_edges = np.histogram(self.blurred_image, bins=256, range=(0.0, 1.0))
        #loaded histogram, set parameters
        fig,ax = plt.subplots()
        plt.plot(bin_edges[0:-1], histogram)
        plt.title("Grayscale Histogram")
        plt.xlabel("grayscale value")
        plt.xlabel("pixels")
        plt.xlim(0, 1.0)
        plt.show()
        #does this even work?
        plt.savefig("./out/histogram.jpg")

    def thresholdFilter(self, threshold=.3):
        print("making masked image")
        self.binary_mask = self.blurred_image < threshold
        plt.imsave("./out/binary_mask.jpg", self.binary_mask, cmap="gray")

    ############## SHOW METHODS #################
    def showLoadedImage(self):
        if (self.inputType == "Color"):
            plt.imshow(self.image)
        elif (self.inputType == "Grayscale"):
            plt.imshow(self.gray_image, cmap="gray")
        else:
            print("error!!")
    
    def showBlurredImage(self):
        plt.imshow(self.blurred_image, cmap="gray")

    def showBinaryMask(self):
        plt.imshow(self.binary_mask, cmap="gray")
        