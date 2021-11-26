from rembg.bg import remove
import numpy as np
import io
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def extract(input_img,output_img):

    input_path = input_img
    output_path = output_img

    f = np.fromfile(input_path)
    result = remove(f)
    img = Image.open(io.BytesIO(result)).convert("RGBA")
    img.save(output_path)
extract("uploads\\a.jpg","b.png")