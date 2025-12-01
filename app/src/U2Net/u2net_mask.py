import os
from pathlib import Path
from skimage import transform
import torch
import torchvision
from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms#, utils

import numpy as np
from PIL import Image

from .data_loader import RescaleT
from .data_loader import ToTensorLab
from .data_loader import SalObjDataset

from .model import U2NET # full size version 173.6 MB
from .model import U2NETP # small version u2net 4.7 MB
import psutil, os, tracemalloc, time

process = psutil.Process(os.getpid())

def mem(tag):
    rss = process.memory_info().rss / (1024 * 1024)
    print(f"[{tag}]  RAM: {rss:.1f} MB")

# normalize the predicted SOD probability map
def normPRED(d):
    ma = torch.max(d)
    mi = torch.min(d)

    dn = (d-mi)/(ma-mi)

    return dn

def get_mask(pred,shape):

    predict = pred
    predict = predict.squeeze()
    predict_np = predict.cpu().data.numpy() #320x320 numpy.ndarray 2D
    im = Image.fromarray(predict_np*255).convert('RGB') #PIL.Image.Image
    imo = im.resize((shape[1],shape[0]),resample=Image.BILINEAR)#PIL.Image.Image
    pb_np = np.array(imo)#numpy.ndarray 3D
    return pb_np

def create_mask(image_orig):
    tracemalloc.start()
    # --------- 1. get image path and name ---------
    model_name='u2netp'#u2netp
    model_dir = Path(__file__).parent /"saved_models"/model_name/model_name
    model_file = model_dir.with_suffix('.pth')

    # --------- 2. dataloader ---------
    #1. dataloader
    test_salobj_dataset = SalObjDataset(file_list = [image_orig],
                                        lbl_name_list = [],
                                        transform=transforms.Compose([RescaleT(320),
                                                                      ToTensorLab(flag=0)])
                                        )
    test_salobj_dataloader = DataLoader(test_salobj_dataset,
                                        batch_size=1,
                                        shuffle=False,
                                        num_workers=1)

    # --------- 3. model define ---------
    if(model_name=='u2net'):
        print("...load U2NET---173.6 MB")
        net = U2NET(3,1)
    elif(model_name=='u2netp'):
        print("...load U2NEP---4.7 MB")
        net = U2NETP(3,1)

    if torch.cuda.is_available():
        net.load_state_dict(torch.load(model_file))
        net.cuda()
    else:
        net.load_state_dict(torch.load(model_file, map_location='cpu'))
    net.eval()
    
    # --------- 4. inference for each image ---------
    dl_list = list(test_salobj_dataloader)
    data_test = dl_list[0]
    inputs_test = data_test['image']    #
    inputs_test = inputs_test.type(torch.FloatTensor)
    if torch.cuda.is_available():
        inputs_test = Variable(inputs_test.cuda())
    else:
        inputs_test = Variable(inputs_test)
    mem("before nograd")    
    with torch.no_grad():
        d1 = net(inputs_test)[0]
        mem("after getting d1")
        # normalization
        pred = d1[:,0,:,:]
        pred = normPRED(pred)
    mem("before extracting mask")
    mask = get_mask(pred, image_orig.shape) #returns mask
    mem("after extracting mask")
    del d1
    mem("after deleting d1")
    current, peak = tracemalloc.get_traced_memory()
    print(f"Python allocs — current = {current/1e6:.2f} MB, peak = {peak/1e6:.2f} MB")
    tracemalloc.stop()
    return mask
