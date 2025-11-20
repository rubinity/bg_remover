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
    image_file_path = Path(module_path) / 'images' / args.image
    output_path = Path(module_path) / "output" / args.image
    return[image_file_path, output_path]
