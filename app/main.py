from PIL import Image
from pathlib import Path
from .src.input import add_args, get_path
from skimage import data, io
import numpy as np
from .src.U2Net.u2net_mask import create_mask
from fastapi import APIRouter, FastAPI, File, UploadFile
from pydantic import BaseModel
from typing import Annotated
from fastapi.responses import Response

app = FastAPI()


# goes to an endpoint
def remove_bg(file: bytes):
    args = add_args()
    [image_file_path, output_path] = get_path(args)
    with Image.open(image_file_path) as img:
        image_orig = io.imread(image_file_path) # numpy array using skimage
        img_mask = create_mask(image_file_path, image_orig.shape)  # numpy array
        image_orig[img_mask[:,:,:] < 80] = 255
        # todo: improve thresholding method
        io.imsave(output_path, image_orig)
    return

@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    # with open("uploads/temp.jpg", "wb") as f:
    #     f.write(file)
    # with open("uploads/temp.jpg", "rb") as f:
    #     upfile = f.read()
    upfile = remove_bg(file)
    return Response(content=upfile)

# create a main for fastapi


if __name__ == "__main__":
    main()