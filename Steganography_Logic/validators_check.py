import numpy as np
from PIL import Image


def max_capacity(image: Image.Image) -> int:
    #Return maximum storable bytes in an image using LSB
    img_array = np.array(image)
    # Each pixel holds 1 bit → 8 pixels = 1 byte
    return img_array.size // 8  


def check_capacity(image: Image.Image, data: bytes) -> bool:
    #Check if the image has enough space for the data
    # +20 buffer for delimiter
    return len(data) + 20 < max_capacity(image)  
