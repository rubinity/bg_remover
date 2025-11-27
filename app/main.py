from PIL import Image
from pathlib import Path
from .src.input import add_args, get_path
from skimage import data
import numpy as np
from .src.U2Net.u2net_mask import create_mask
from fastapi import APIRouter, FastAPI, File, UploadFile
from pydantic import BaseModel
from typing import Annotated
from fastapi.responses import Response
import io

app = FastAPI()

@app.get("/")
async def root():
    msg = "The server is running"
    return Response(content=msg)


def get_bytes(pil_image):
    with io.BytesIO() as output_stream:
        pil_image.save(output_stream, format="JPEG")
        output_stream.seek(0)
        upfile = output_stream.read()
    return upfile

# goes to an endpoint
def remove_bg(file: bytes):
    # args = add_args()
    # [image_file_path, output_path] = get_path(args)
    pil_file = io.BytesIO(file)
    with Image.open(pil_file) as img:
        # image_orig = io.imread(image_file_path) # numpy array using skimage
        image_orig = np.array(img)
        img_mask = create_mask(image_orig)  # numpy array
        image_orig[img_mask[:,:,:] < 80] = 255
        pil_image = Image.fromarray(image_orig) #PIL.Image.Image
        upfile = get_bytes(pil_image)
        # todo: improve thresholding method 
        # io.imsave(output_path, image_orig)
    return upfile

@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    upfile = remove_bg(file)
    # with io.BytesIO(file) as stream: #stream
    #     with Image.open(stream) as img:
    #         image_orig = np.array(img)
    #         upfile = get_bytes(img)
        
    return Response(content=upfile)


    # return {"message": "tft"}
# @app.post("/files/")
# async def create_file(file: Annotated[bytes, File()]):
    # with open("uploads/temp.jpg", "wb") as f:
    #     f.write(file)
    # with open("uploads/temp.jpg", "rb") as f:
    #     upfile = f.read()
    upfile = remove_bg(file)
    return Response(content=upfile)

# create a main for fastapi
# def main():
#     # import uvicorn
#     # uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()