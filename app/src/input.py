from pathlib import Path
from argparse import ArgumentParser

def add_args():
    parser = ArgumentParser(prog='Background remover',
                    description='removes background',
                    epilog='See you!',)
    parser.add_argument('image')
    args = parser.parse_args()
    return args

def get_path(args):
    module_path = str(Path(__file__).parent.parent)
    image_path = module_path+'\\images\\'+ args.image
    output_path = module_path+"\\output\\i.jpg"
    return[image_path, output_path]
