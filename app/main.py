from PIL import Image
import numpy as np
from .src.U2Net.u2net_mask import create_mask
from .src.U2Net.mem_calc import process, mem, saved_mem
from fastapi import APIRouter, FastAPI, File
from typing import Annotated
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
# from .src.U2Net.u2net_mask
import io, tracemalloc

pixels = {}
pixels["photo"] = 0
app = FastAPI()
# Allow CORS for all origins (you can restrict to specific domains if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (you can specify a list of domains here, e.g. ["http://localhost:3000"])
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
async def root():
    msg = "The server is running"
    return Response(content=msg)

# convert PIL image to bytes
def get_bytes(pil_image):
    with io.BytesIO() as output_stream:
        pil_image.save(output_stream, format="JPEG")
        output_stream.seek(0)
        upfile = output_stream.read()
    return upfile

# goes to an endpoint
def remove_bg(file: bytes):
    tracemalloc.start()
    max_pix = 10000000
    pil_file = io.BytesIO(file)
    with Image.open(pil_file) as img:
        (length, height) = img.size
        pixs = length * height
        pixels["photo"] = pixs/1000000
        scale = 0
        if pixs > max_pix:   
            scale = (max_pix/pixs)**0.5
            img = img.resize((int(length * scale), int(height * scale)))
        image_orig = np.array(img.convert('RGB'))  # numpy array
        img_mask = create_mask(image_orig)  # numpy array
        image_orig[img_mask[:,:,:] < 80] = 255
        pil_image = Image.fromarray(image_orig) #PIL.Image.Image
        if scale != 0:
            pil_image = pil_image.resize((length, height))
        upfile = get_bytes(pil_image)  
        # todo: improve thresholding method
        current, peak = tracemalloc.get_traced_memory()
        print(f"Python allocs — current = {current/1e6:.2f} MB, peak = {peak/1e6:.2f} MB")
        tracemalloc.stop()
    return upfile

@app.get("/metrics")
async def metrics():
    content = ""
    for tag in saved_mem:
        content = content + tag + " " + str(saved_mem[tag]) + "\n"
    content = content + "pixels" + " " + str(pixels["photo"]) + "\n"
    return Response(content, media_type="text/plain; version=0.0.4")

@app.post("/remove-background")
async def create_file(file: Annotated[bytes, File()]):
    upfile = remove_bg(file)
    return Response(content=upfile, media_type="image/jpeg") 