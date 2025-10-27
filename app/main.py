from PIL import Image
from .src.input import add_args, get_path

def main():
    args = add_args()
    [image_path, output_path] = get_path(args)
    img = Image.open(image_path)
    print('before:', img.height, 'x', img.width)
    img1 = img.resize([img.width//2, img.height//2],)
    print('after: ', img1.height, 'x', img1.width)
    img1.save(output_path)
    img.close()
    img1.close()

if __name__ == "__main__":
    main()