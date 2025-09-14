import numpy as np
from PIL import Image

#To mark the end of the text
delimiter = b"<END_OF_DATA>"

#Encode the file/text inside the Image
def encode(image : Image.Image, data : bytes) -> Image.Image:
    if isinstance(data, str):
        data = data.encode()   # convert str → bytes

    img_num_array = np.array(image)      
    flatten_img = img_num_array.flatten()
    payload = data + delimiter
    
    #Convert Payload data into bit string
    bits = ''.join([f"{byte:08b}" for byte in payload])
    
    if len(bits) > len(flatten_img) :
        raise ValueError("Data is too large to encode inside the Image!")
    
    for i, bit in enumerate(bits):
        flatten_img[i] = (flatten_img[i] & 0b11111110 | int(bit))

    #Reshape to Orginal Image
    stego_array = flatten_img.reshape(img_num_array.shape)
    #Type (np.uint8) = to ensure pixel values are valid(0-255)
    return Image.fromarray(stego_array.astype(np.uint8))

def decode(stego_Image: Image.Image) -> bytes:

    img_num_array = np.array(stego_Image)
    flatten_img = img_num_array.flatten()
    
    #To Extract Least Significant bits
    bits = [str(pixel & 1) for pixel in flatten_img]
    bit_string = ''.join(bits)

    #bytearray() = represent array of int in range 0 to 255
    #
    data = bytearray()
    for i in range(0, len(bit_string), 8):
        byte = bit_string[i:i+8]
        if(len(byte)<8):
            break
        data.append(int(byte, 2))

    #Checks and stops if delimited is found
    idx = data.find(delimiter)
    if idx != -1:
        return bytes(data[:idx])
    
    #return empty, if no delimiter is found
    return b""




 
