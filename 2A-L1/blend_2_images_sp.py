import cv2
import numpy as np


# Blend two images
def blend(a, b, alpha):
    """ Blends to images using a weight factor.
    Args:
        a (numpy.array): Image A.
        b (numpy.array): Image B.
        alpha (float): Weight factor.

    Returns:
        numpy.array: Blended Image.
    """
    return alpha * (a + b)

def weightlessBlend(a, b, alpha):
    """ Blends to images using a weight factor.
    Args:
        a (numpy.array): Image A.
        b (numpy.array): Image B.
        alpha (float): Weight factor.

    Returns:
        numpy.array: Blended Image.
    """
    return a + b

def directBlend(a, b, alpha):
    """ Blends to images using a weight factor.
    Args:
        a (numpy.array): Image A.
        b (numpy.array): Image B.
        alpha (float): Weight factor.

    Returns:
        numpy.array: Blended Image.
    """
    return  (alpha * a) + (alpha * b)

dolphin = cv2.imread("images/dolphin.png")
bicycle = cv2.imread("images/bicycle.png")

result = blend(dolphin, bicycle, 0.75)
cv2.imshow('alpha * (a + b)', result.astype(np.uint8))

result = weightlessBlend(dolphin, bicycle, 0.75)
cv2.imshow('a + b', result.astype(np.uint8))

result = directBlend(dolphin, bicycle, 0.75)
cv2.imshow('(alpha * a) + (alpha * b)', result.astype(np.uint8))
cv2.waitKey(0)
