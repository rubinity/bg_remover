import os
from pathlib import Path
from skimage import io, transform
import torch
import torchvision
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms#, utils
# import torch.optim as optim

import numpy as np
from PIL import Image
import glob

from .data_loader import RescaleT
from .data_loader import ToTensor
from .data_loader import ToTensorLab
from .data_loader import SalObjDataset

from .model import U2NET # full size version 173.6 MB
from .model import U2NETP # small version u2net 4.7 MB

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
    # todo take directly
    imo = im.resize((shape[1],shape[0]),resample=Image.BILINEAR)#PIL.Image.Image
    pb_np = np.array(imo)#numpy.ndarray 3D
    return pb_np

def create_mask(image_file_path, shape):

    # --------- 1. get image path and name ---------
    model_name='u2net'#u2netp
    prediction_dir = Path(image_file_path).parent.parent /"output"
    model_dir = Path(__file__).parent /"saved_models"/model_name/model_name
    model_file = model_dir.with_suffix('.pth')
    img_name_list = glob.glob(str(Path(image_file_path)))#this will be one file list

    # --------- 2. dataloader ---------
    #1. dataloader
    # img_name_list should be the list of files, for now one file
    test_salobj_dataset = SalObjDataset(img_name_list = img_name_list,
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

    d1,d2,d3,d4,d5,d6,d7= net(inputs_test)

        # normalization
    pred = d1[:,0,:,:]
    pred = normPRED(pred)

        # save results to test_results folder
    if not os.path.exists(prediction_dir):
        os.makedirs(prediction_dir, exist_ok=True)
    mask = get_mask(pred, shape) #returns mask
    del d1,d2,d3,d4,d5,d6,d7
    return mask
