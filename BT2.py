import numpy as np
import cv2
import matplotlib.pyplot as plt

def pinholeCamera(imageSize=(400, 400), pinholeSize=(3, 3), objectPosition=(200, 200), objectSize=(20, 200)):
    image = np.zeros((imageSize[0], imageSize[1], 3), dtype=np.uint8)

    pinholeStart = (objectPosition[0] - pinholeSize[0] // 2, objectPosition[1] - pinholeSize[1] // 2)
    pinholeEnd = (pinholeStart[0] + pinholeSize[0], pinholeStart[1] + pinholeSize[1])
    image[pinholeStart[1]:pinholeEnd[1], pinholeStart[0]:pinholeEnd[0]] = (255, 255, 255)

    candleStart = (objectPosition[0] - objectSize[0] // 2, objectPosition[1] - objectSize[1] // 2)
    candleEnd = (candleStart[0] + objectSize[0], candleStart[1] + objectSize[1])
    image[candleStart[1]:candleEnd[1], candleStart[0]:candleEnd[0]] = (0, 165, 255)

    return image

def plotImages(images, titles):
    fig, axes = plt.subplots(1, len(images), figsize=(12, 4))
    for ax, image, titles in zip(axes, images, titles):
        ax.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        ax.set_title(titles)
        ax.axis('off')
    plt.show()

pinholeSize = (10, 10)

# Generate images
image1 = pinholeCamera(imageSize=(400, 400), pinholeSize=pinholeSize, objectPosition=(200, 200), objectSize=(20, 200))
image2 = pinholeCamera(imageSize=(400, 400), pinholeSize=pinholeSize, objectPosition=(300, 300), objectSize=(20, 200))

# Plot images
plotImages([image1, image2], ['Pinhole Camera Model 1', 'Pinhole Camera Model 2'])