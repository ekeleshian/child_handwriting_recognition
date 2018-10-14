# -*- coding: utf-8 -*-
"""
Helper functions for ocr project
"""
import matplotlib.pyplot as plt
import numpy as np
import cv2

SMALL_HEIGHT = 800

   
def resize(img, height=SMALL_HEIGHT, allways=False):
    """ Resize image to given height """
    if (img.shape[0] > height or allways):
        rat = height / img.shape[0]
        return cv2.resize(img, (int(rat * img.shape[1]), height))
    
    return img


def ratio(img, height=SMALL_HEIGHT):
    """ Getting scale ratio """
    return img.shape[0] / height


def extendImg(img, shape):
    """ Extend 2D image (numpy array) in vertical and horizontal direction
    Shape of result image will match 'shape'
    Args:
        img: image to be extended
        shape: shape (touple) of result image
    Returns:
        Extended image
    """
    x = np.zeros(shape, np.uint8)
    x[:img.shape[0], :img.shape[1]] = img
    return x

def display_image(img, cmap=None):
    dpi = 80
    margin = 0.05 # (5% of the width/height of the figure...)
    xpixels, ypixels = 800, 800

    # Make a figure big enough to accomodate an axis of xpixels by ypixels
    # as well as the ticklabels, etc...
    figsize = (1 + margin) * ypixels / dpi, (1 + margin) * xpixels / dpi

    fig = plt.figure(figsize=figsize, dpi=dpi)
    # Make the axis the right size...
    ax = fig.add_axes([margin, margin, 1 - 2*margin, 1 - 2*margin])

    ax.imshow(img, cmap=cmap)
    plt.show()
    return print("loaded")
